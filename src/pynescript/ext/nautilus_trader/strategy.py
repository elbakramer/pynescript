# Copyright 2024 Yunseong Hwang
#
# Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/lgpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

from nautilus_trader.config import StrategyConfig
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import BarType
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.instruments import Instrument
from nautilus_trader.trading.strategy import Strategy


class PinescriptStrategyConfig(StrategyConfig):
    instrument_id: InstrumentId
    bar_type: BarType


class PinescriptStrategy(Strategy):
    def __init__(self, config: PinescriptStrategyConfig):
        super().__init__(config)
        self.instrument_id = config.instrument_id
        self.bar_type = config.bar_type
        self.instrument: Instrument | None = None

    def on_start(self):
        self.instrument = self.cache.instrument(self.instrument_id)
        self.request_bars(self.bar_type)
        self.subscribe_bars(self.bar_type)
        self.subscribe_trade_ticks(self.instrument_id)

    def on_bar(self, bar: Bar):
        pass

    def on_trade_tick(self, tick: TradeTick):
        pass

    def on_stop(self):
        self.cancel_all_orders(self.instrument_id)
        self.close_all_positions(self.instrument_id)
        self.unsubscribe_bars(self.bar_type)

    def on_reset(self):
        pass
