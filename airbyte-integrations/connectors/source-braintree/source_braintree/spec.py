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
from enum import Enum

from pydantic import BaseModel, Field, validator


class Environment(str, Enum):
    DEV = "development"
    SANDBOX = "sandbox"


class BraintreeConfig(BaseModel):
    class Config:
        title = "Braintree Spec"
        doc_url = "https://docs.airbyte.io/integrations/sources/braintree"

    merchant_id: str = Field(name="Merchant ID", description="")
    public_key: str = Field(name="Public key", description="")
    private_key: str = Field(name="Private Key", description="", airbyte_secret=True)
    start_date: datetime = Field(name="Start date", description="")
    environment: Environment = Field(name="Environment", description="", examples=["sandbox", "production", "qa"])

    @validator("environment", pre=True)
    def check_lower_case(cls, v):
        return v.lower()

    @classmethod
    def schema(cls, **kvargs):
        schema = super().schema(**kvargs)
        schema["properties"] = {name: desc for name, desc in schema["properties"].items() if not name.startswith("_")}
        return {
            "documentationUrl": cls.Config.doc_url,
            "connectionSpecification": schema,
        }
