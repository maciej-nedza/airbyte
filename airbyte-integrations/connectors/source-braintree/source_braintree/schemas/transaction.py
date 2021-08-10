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

from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel

from .cards import Address, AndroidPayCard, ApplePayCard, CreditCard
from .common import AllOptional
from .customer import Customer
from .discount import Discount
from .dispute import Dispute


class AddressOptional(Address, metaclass=AllOptional):
    pass


class CustomerOptional(Customer, metaclass=AllOptional):
    pass


class CreditCardOptional(CreditCard, metaclass=AllOptional):
    pass


class DisbursementDetails(BaseModel, metaclass=AllOptional):
    disbursement_date: date
    funds_held: bool
    settlement_amount: Decimal
    settlement_base_currency_exchange_rate: Decimal
    settlement_currency_exchange_rate: Decimal
    settlement_currency_iso_code: str
    success: bool


class StatusHistoryDetails(BaseModel):
    amount: Decimal
    status: str
    timestamp: datetime
    transaction_source: str
    user: Optional[str]


class SubscriptionDetails(BaseModel):
    billing_period_end_date: Optional[datetime]
    billing_period_start_date: Optional[datetime]


class Transaction(BaseModel):
    acquirer_reference_number: Optional[str]
    additional_processor_response: Optional[str]
    amount: str
    android_pay_card_details: Optional[AndroidPayCard]
    apple_pay_details: Optional[ApplePayCard]
    authorization_expires_at: datetime
    avs_error_response_code: Optional[str]
    avs_postal_code_response_code: str
    avs_street_address_response_code: str
    billing_details: Optional[AddressOptional]
    channel: Optional[str]
    created_at: datetime
    credit_card_details: Optional[CreditCardOptional]
    currency_iso_code: str
    custom_fields: str
    customer_details: CustomerOptional
    cvv_response_code: str
    disbursement_details: DisbursementDetails
    discount_amount: Optional[Decimal]
    discounts: List[Discount]
    disputes: List[Dispute]
    escrow_status: Optional[str]
    gateway_rejection_reason: Optional[str]
    global_id: str
    graphql_id: str
    id: str
    installment_count: Optional[Decimal]
    merchant_account_id: str
    merchant_address: Optional[AddressOptional]
    merchant_identification_number: str
    merchant_name: str
    network_response_code: str
    network_response_text: str
    network_transaction_id: str
    order_id: str
    payment_instrument_type: str
    pin_verified: bool
    plan_id: Optional[str]
    processed_with_network_token: bool
    processor_authorization_code: str
    processor_response_code: str
    processor_response_text: str
    processor_response_type: str
    processor_settlement_response_code: str
    processor_settlement_response_text: str
    purchase_order_number: str
    recurring: bool
    refund_ids: List[str]
    refund_global_ids: List[str]
    refunded_transaction_id: Optional[str]
    response_emv_data: Optional[str]
    retrieval_reference_number: str
    sca_exemption_requested: Optional[str]
    service_fee_amount: Optional[Decimal]
    settlement_batch_id: Optional[str]
    shipping_amount: Optional[Decimal]
    shipping_details: Optional[AddressOptional]
    ships_from_postal_code: Optional[str]
    status: str
    status_history: List[StatusHistoryDetails]
    subscription_details: Optional[SubscriptionDetails]
    subscription_id: Optional[str]
    tax_amount: Optional[Decimal]
    tax_exempt: bool
    terminal_identification_number: str
    type: str
    updated_at: datetime
    voice_referral_number: Optional[str]
