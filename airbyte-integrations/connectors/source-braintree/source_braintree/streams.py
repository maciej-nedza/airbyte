#
# MIT License
#
# Copyright (c) 2020 Airbyte
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from abc import abstractmethod, abstractproperty
from datetime import datetime
from typing import Any, Iterable, List, Mapping, Optional, Union

import braintree
from airbyte_cdk.models import SyncMode
from airbyte_cdk.sources.streams.core import Stream
from braintree.attribute_getter import AttributeGetter
from source_braintree.schemas import Customer, Discount, Dispute, MerchantAccount, Plan, Subscription, Transaction
from source_braintree.spec import BraintreeConfig


class BraintreeStream(Stream):
    """
    Pass
    """

    def __init__(self, config: BraintreeConfig):
        self._gateway = BraintreeStream.create_gateway(config)

    @staticmethod
    def create_gateway(config: BraintreeConfig):
        return braintree.BraintreeGateway(braintree.Configuration(**config.dict()))

    @abstractproperty
    def model(self):
        """
        Pydantic model to represent catalog schema
        """

    @abstractmethod
    def get_items(self):
        """
        braintree SDK gateway object for items list
        """

    def get_json_schema(self):
        return self.model.schema()

    def stream_slices(
        self,
        sync_mode: SyncMode,
        cursor_field: List[str] = None,
        stream_state: Mapping[str, Any] = None,
    ) -> Iterable[Optional[Mapping[str, Any]]]:
        return [None]

    def get_updated_state(
        self,
        current_stream_state: Mapping[str, Any],
        latest_record: Mapping[str, Any],
    ):
        return {}

    @staticmethod
    def get_json_from_resource(resource_obj: Union[AttributeGetter, List[AttributeGetter]]):

        if isinstance(resource_obj, list):
            return [obj if not isinstance(obj, AttributeGetter) else BraintreeStream.get_json_from_resource(obj) for obj in resource_obj]
        obj_dict = resource_obj.__dict__
        return {
            attr: obj_dict[attr]
            if not isinstance(obj_dict[attr], (AttributeGetter, list))
            else BraintreeStream.get_json_from_resource(obj_dict[attr])
            for attr in obj_dict
            if not attr.startswith("_") and attr != "gateway"
        }

    def read_records(
        self,
        sync_mode: SyncMode,
        cursor_field: List[str] = None,
        stream_slice: Mapping[str, Any] = None,
        stream_state: Mapping[str, Any] = None,
    ) -> Iterable[Mapping[str, Any]]:
        items = self.get_items()
        for item in items:
            item = self.get_json_from_resource(item)
            item = self.model(**item)
            yield item.dict(exclude_unset=True)
        yield from []


class CustomerStream(BraintreeStream):
    """
    https://developer.paypal.com/braintree/docs/reference/request/customer/search
    """

    primary_key = "id"
    model = Customer
    cursor_field = "created_at"

    def get_items(self):
        return self._gateway.customer.all()


class DiscountStream(BraintreeStream):
    """
    https://developer.paypal.com/braintree/docs/reference/response/discount
    """

    primary_key = "id"
    model = Discount

    def get_items(self):
        return self._gateway.discount.all()


class DisputeStream(BraintreeStream):
    """
    https://developer.paypal.com/braintree/docs/reference/request/dispute/search
    """

    primary_key = "id"
    model = Dispute

    def get_items(self):
        return self._gateway.dispute.all()


class TransactionStream(BraintreeStream):
    """
    https://developer.paypal.com/braintree/docs/reference/response/transaction
    """

    primary_key = "id"
    model = Transaction

    def get_items(self):
        return self._gateway.transaction.search(braintree.TransactionSearch.created_at >= datetime(2019, 1, 1))


class MerchantAccountStream(BraintreeStream):
    """
    https://developer.paypal.com/braintree/docs/reference/response/merchant-account
    """

    primary_key = "id"
    model = MerchantAccount

    def get_items(self):
        return self._gateway.merchant_account.all().merchant_accounts


class PlanStream(BraintreeStream):
    """
    https://developer.paypal.com/braintree/docs/reference/response/plan
    """

    primary_key = "id"
    model = Plan

    def get_items(self):
        return self._gateway.plan.all()


class SubscriptionStream(BraintreeStream):
    """
    https://developer.paypal.com/braintree/docs/reference/response/subscription
    """

    primary_key = "id"
    model = Subscription

    def get_items(self):
        return self.subscription.search(braintree.SubscriptionSearch.created_at >= datetime(2019, 1, 1)).items
