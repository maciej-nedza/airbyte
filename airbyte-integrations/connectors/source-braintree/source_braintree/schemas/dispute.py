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
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel


class Evidence(BaseModel):
    created_at: datetime
    id: str
    sent_to_processor_at: datetime
    url: Optional[str]
    comment: Optional[str]


class PaypalMessage(BaseModel):
    message: str
    send_at: datetime
    sender: str


class Dispute(BaseModel):
    amount_disputed: Decimal
    amount_won: Decimal
    case_number: str
    chargeback_protection_level: str
    created_at: datetime
    currency_iso_code: str
    evidence: Evidence
    graphql_id: str
    id: str
    kind: str
    merchant_account_id: str
    original_dispute_id: str
    paypal_messages: List[PaypalMessage]
    processor_comments: str
    reason: str
    reason_code: str
    reason_description: str
    received_date: datetime
    reference_number: str
    reply_by_date: datetime
    status: str
    updated_at: datetime
