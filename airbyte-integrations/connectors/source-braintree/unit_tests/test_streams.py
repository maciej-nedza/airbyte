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
import responses
from source_braintree.spec import BraintreeConfig
from source_braintree.streams import CustomerStream, DiscountStream, MerchantAccountStream, PlanStream, TransactionStream


def load_file(fn):
    return open(fn).read()


@responses.activate
def test_customers_stream(test_config):
    responses.add(
        responses.POST,
        "https://api.sandbox.braintreegateway.com:443/merchants/mech_id/customers/advanced_search_ids",
        body=load_file("unit_tests/customers_ids.txt"),
    )
    responses.add(
        responses.POST,
        "https://api.sandbox.braintreegateway.com:443/merchants/mech_id/customers/advanced_search",
        body=load_file("unit_tests/customers_obj_response.txt"),
    )
    config = BraintreeConfig(**test_config)
    stream = CustomerStream(config)
    records = [r for r in stream.read_records(None, None, None)]
    assert len(records) == 1


@responses.activate
def test_transaction_stream(test_config):
    responses.add(
        responses.POST,
        "https://api.sandbox.braintreegateway.com:443/merchants/mech_id/transactions/advanced_search_ids",
        body=load_file("unit_tests/transaction_ids.txt"),
    )
    responses.add(
        responses.POST,
        "https://api.sandbox.braintreegateway.com:443/merchants/mech_id/transactions/advanced_search",
        body=load_file("unit_tests/transaction__objs.txt"),
    )
    config = BraintreeConfig(**test_config)
    stream = TransactionStream(config)
    records = [r for r in stream.read_records(None, None, None)]
    assert len(records) == 2


@responses.activate
def test_discount(test_config):
    responses.add(
        responses.GET,
        "https://api.sandbox.braintreegateway.com:443/merchants/mech_id/discounts/",
        body=load_file("unit_tests/discounts.txt"),
    )
    config = BraintreeConfig(**test_config)
    stream = DiscountStream(config)
    records = [r for r in stream.read_records(None, None, None)]
    assert len(records) == 1


@responses.activate
def test_merch_account(test_config):
    responses.add(
        responses.GET,
        "https://api.sandbox.braintreegateway.com:443/merchants/mech_id/merchant_accounts/",
        body=load_file("unit_tests/merch_account.txt"),
    )
    config = BraintreeConfig(**test_config)
    stream = MerchantAccountStream(config)
    records = [r for r in stream.read_records(None, None, None)]
    assert len(records) == 1


@responses.activate
def test_plan(test_config):
    responses.add(
        responses.GET,
        "https://api.sandbox.braintreegateway.com:443/merchants/mech_id/plans/",
        body=load_file("unit_tests/plans.txt"),
    )
    config = BraintreeConfig(**test_config)
    stream = PlanStream(config)
    records = [r for r in stream.read_records(None, None, None)]
    assert len(records) == 1
