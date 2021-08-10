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
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Address(BaseModel):
    company: str
    country_code_alpha2: str
    country_code_alpha3: str
    country_code_numeric: str
    country_name: str
    created_at: datetime
    customer_id: str
    extended_address: str
    first_name: str
    id: str
    last_name: str
    locality: str
    postal_code: str
    region: str
    street_address: str
    updated_at: datetime


class CreditCard(BaseModel):
    billing_address: Optional[Address]
    bin: str
    card_type: str
    cardholder_name: str
    commercial: str
    country_of_issuance: str
    created_at: datetime
    customer_id: str
    customer_location: str
    debit: str
    default: bool
    durbin_regulated: str
    expiration_date: Optional[str]
    expiration_month: str
    expiration_year: str
    expired: bool
    healthcare: str
    image_url: str
    issuing_bank: str
    last_4: str
    masked_number: Optional[str]
    payroll: str
    prepaid: str
    product_id: str
    subscriptions: List[str]
    token: str
    unique_number_identifier: str
    updated_at: datetime


class ApplePayCard(CreditCard):
    source_description: str


class AndroidPayCard(CreditCard):
    google_transaction_id: str
    source_card_type: str
    source_description: str
    is_network_tokenized: bool
    virtual_card_last_4: str
    virtual_card_type: str
