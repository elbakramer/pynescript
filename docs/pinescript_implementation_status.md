# PineScript v6 Implementation Index

This document tracks the implementation status of PineScript v6 features in pynescript.

## Legend
- ✅ Implemented
- ❌ Not implemented
- 🔄 Partially implemented
- ❓ Unknown/Needs verification

## Variables (Built-in Series)

### Price Data
- ✅ close
- ✅ open
- ✅ high
- ✅ low
- ✅ volume
- ✅ time
- ✅ hl2
- ✅ hlc3
- ✅ hlcc4
- ✅ ohlc4

### Time
- ✅ year
- ✅ month
- ✅ weekofyear
- ✅ dayofmonth
- ✅ dayofweek
- ✅ hour
- ✅ minute
- ✅ second
- ✅ time_close
- ✅ time_tradingday
- ✅ timenow

### Chart State
- ✅ bar_index
- ✅ barstate.isconfirmed
- ✅ barstate.isfirst
- ✅ barstate.ishistory
- ✅ barstate.islast
- ✅ barstate.islastconfirmedhistory
- ✅ barstate.isnew
- ✅ barstate.isrealtime
- ✅ last_bar_index
- ✅ last_bar_time

### Symbol Info
- ✅ syminfo.ticker
- ✅ syminfo.tickerid
- ✅ syminfo.currency
- ✅ syminfo.basecurrency
- ✅ syminfo.description
- ✅ syminfo.type
- ✅ syminfo.root
- ✅ syminfo.prefix
- ✅ syminfo.suffix
- ✅ syminfo.mintick
- ✅ syminfo.minmove
- ✅ syminfo.pointvalue
- ✅ syminfo.session
- ✅ syminfo.timezone
- ✅ syminfo.volumetype
- ✅ syminfo.pricescale
- ✅ syminfo.mincontract
- ✅ syminfo.employees
- ✅ syminfo.sector
- ✅ syminfo.industry
- ✅ syminfo.country
- ✅ syminfo.shareholders
- ✅ syminfo.shares_outstanding_total
- ✅ syminfo.shares_outstanding_float
- ✅ syminfo.earnings_per_share
- ✅ syminfo.dividends_per_share
- ✅ syminfo.market_capitalization
- ✅ syminfo.target_price_average
- ✅ syminfo.target_price_median
- ✅ syminfo.target_price_high
- ✅ syminfo.target_price_low
- ✅ syminfo.target_price_estimates
- ✅ syminfo.target_price_date
- ✅ syminfo.main_tickerid
- ✅ syminfo.expiration_date
- ✅ syminfo.current_contract

### Session
- ✅ session.regular
- ✅ session.extended
- ✅ session.ismarket
- ✅ session.ispremarket
- ✅ session.ispostmarket
- ✅ session.isfirstbar
- ✅ session.isfirstbar_regular
- ✅ session.islastbar
- ✅ session.islastbar_regular

### Dividends/Earnings
- ✅ dividends.future_amount
- ✅ dividends.future_ex_date
- ✅ dividends.future_pay_date
- ✅ dividends.gross
- ✅ dividends.net
- ✅ earnings.future_eps
- ✅ earnings.future_period_end_time
- ✅ earnings.future_revenue
- ✅ earnings.future_time
- ✅ earnings.actual
- ✅ earnings.estimate
- ✅ earnings.standardized

### Strategy
- ✅ strategy.position_size
- ✅ strategy.position_avg_price
- ✅ strategy.position_entry_name
- ✅ strategy.opentrades
- ✅ strategy.closedtrades
- ✅ strategy.wintrades
- ✅ strategy.losstrades
- ✅ strategy.eventrades
- ✅ strategy.grossprofit
- ✅ strategy.grossprofit_percent
- ✅ strategy.grossloss
- ✅ strategy.grossloss_percent
- ✅ strategy.netprofit
- ✅ strategy.netprofit_percent
- ✅ strategy.openprofit
- ✅ strategy.openprofit_percent
- ✅ strategy.avg_trade
- ✅ strategy.avg_trade_percent
- ✅ strategy.avg_winning_trade
- ✅ strategy.avg_winning_trade_percent
- ✅ strategy.avg_losing_trade
- ✅ strategy.avg_losing_trade_percent
- ✅ strategy.max_runup
- ✅ strategy.max_runup_percent
- ✅ strategy.max_drawdown
- ✅ strategy.max_drawdown_percent
- ✅ strategy.initial_capital
- ✅ strategy.equity
- ✅ strategy.margin_liquidation_price
- ✅ strategy.account_currency
- ✅ strategy.convert_to_account
- ✅ strategy.convert_to_symbol
- ✅ strategy.max_contracts_held_all
- ✅ strategy.max_contracts_held_long
- ✅ strategy.max_contracts_held_short
- ✅ strategy.closedtrades.first_index
- ✅ strategy.risk.allow_entry_in
- ✅ strategy.risk.max_cons_loss_days
- ✅ strategy.risk.max_drawdown
- ✅ strategy.risk.max_intraday_filled_orders
- ✅ strategy.risk.max_intraday_loss
- ✅ strategy.risk.max_position_size
- ✅ strategy.cash
- ✅ strategy.fixed
- ✅ strategy.percent_of_equity
- ✅ strategy.long
- ✅ strategy.short
- ✅ strategy.direction.all
- ✅ strategy.direction.long
- ✅ strategy.direction.short
- ✅ strategy.default_entry_qty
- ✅ strategy.commission.cash_per_contract
- ✅ strategy.commission.cash_per_order
- ✅ strategy.commission.percent
- ✅ strategy.oca.cancel
- ✅ strategy.oca.none
- ✅ strategy.oca.reduce

### Chart
- ✅ chart.bg_color
- ✅ chart.fg_color
- ✅ chart.is_heikinashi
- ✅ chart.is_kagi
- ✅ chart.is_linebreak
- ✅ chart.is_pnf
- ✅ chart.is_range
- ✅ chart.is_renko
- ✅ chart.is_standard
- ✅ chart.left_visible_bar_time
- ✅ chart.right_visible_bar_time

### Timeframe
- ✅ timeframe.period
- ✅ timeframe.multiplier
- ✅ timeframe.isseconds
- ✅ timeframe.isminutes
- ✅ timeframe.isdaily
- ✅ timeframe.isweekly
- ✅ timeframe.ismonthly
- ✅ timeframe.isdwm
- ✅ timeframe.isintraday
- ✅ timeframe.isticks
- ✅ timeframe.main_period

### Bid/Ask
- ✅ bid
- ✅ ask

### TA Built-ins
- ✅ ta.accdist
- ✅ ta.iii
- ✅ ta.nvi
- ✅ ta.obv
- ✅ ta.pvi
- ✅ ta.pvt
- ✅ ta.tr
- ✅ ta.vwap
- ✅ ta.wad
- ✅ ta.wvad

### Drawing Objects Collections
- ✅ box.all
- ✅ label.all
- ✅ line.all
- ✅ linefill.all
- ✅ table.all
- ✅ polyline.all

### NA
- ✅ na

## Constants

### Colors
- ✅ color.aqua
- ✅ color.black
- ✅ color.blue
- ✅ color.fuchsia
- ✅ color.gray
- ✅ color.green
- ✅ color.lime
- ✅ color.maroon
- ✅ color.navy
- ✅ color.olive
- ✅ color.orange
- ✅ color.purple
- ✅ color.red
- ✅ color.silver
- ✅ color.teal
- ✅ color.white
- ✅ color.yellow

### Math
- ✅ math.e
- ✅ math.phi
- ✅ math.pi
- ✅ math.rphi

### Plot Styles
- ✅ plot.style_line
- ✅ plot.style_linebr
- ✅ plot.style_stepline
- ✅ plot.style_stepline_diamond
- ✅ plot.style_histogram
- ✅ plot.style_cross
- ✅ plot.style_area
- ✅ plot.style_areabr
- ✅ plot.style_columns
- ✅ plot.style_circles
- ✅ plot.style_steplinebr

### Line Styles
- ✅ line.style_solid
- ✅ line.style_dashed
- ✅ line.style_dotted
- ✅ line.style_arrow_left
- ✅ line.style_arrow_right
- ✅ line.style_arrow_both

### Label Styles
- ✅ label.style_label_down
- ✅ label.style_label_up
- ✅ label.style_label_left
- ✅ label.style_label_right
- ✅ label.style_label_upper_left
- ✅ label.style_label_upper_right
- ✅ label.style_label_lower_left
- ✅ label.style_label_lower_right
- ✅ label.style_label_center
- ✅ label.style_arrowup
- ✅ label.style_arrowdown
- ✅ label.style_flag
- ✅ label.style_circle
- ✅ label.style_square
- ✅ label.style_diamond
- ✅ label.style_text_outline
- ✅ label.style_triangledown
- ✅ label.style_triangleup
- ✅ label.style_xcross
- ✅ label.style_cross
- ✅ label.style_none

### Box Styles
- ✅ (No specific box styles listed)

### Table Styles
- ✅ (No specific table styles listed)

### Positions
- ✅ position.top_left
- ✅ position.top_center
- ✅ position.top_right
- ✅ position.middle_left
- ✅ position.middle_center
- ✅ position.middle_right
- ✅ position.bottom_left
- ✅ position.bottom_center
- ✅ position.bottom_right

### Sizes
- ✅ size.auto
- ✅ size.tiny
- ✅ size.small
- ✅ size.normal
- ✅ size.large
- ✅ size.huge

### Text
- ✅ text.align_left
- ✅ text.align_center
- ✅ text.align_right
- ✅ text.align_top
- ✅ text.align_bottom
- ✅ text.format_none
- ✅ text.format_bold
- ✅ text.format_italic
- ✅ text.wrap_none
- ✅ text.wrap_auto

### Fonts
- ✅ font.family_default
- ✅ font.family_monospace

### Scales
- ✅ scale.left
- ✅ scale.right
- ✅ scale.none

### Display
- ✅ display.none
- ✅ display.pane
- ✅ display.data_window
- ✅ display.price_scale
- ✅ display.status_line
- ✅ display.all

### XLoc
- ✅ xloc.bar_index
- ✅ xloc.bar_time

### YLoc
- ✅ yloc.price
- ✅ yloc.abovebar
- ✅ yloc.belowbar

### Extend
- ✅ extend.none
- ✅ extend.left
- ✅ extend.right
- ✅ extend.both

### HLine Styles
- ✅ hline.style_solid
- ✅ hline.style_dashed
- ✅ hline.style_dotted

### Plot Line Styles
- ✅ plot.linestyle_solid
- ✅ plot.linestyle_dashed
- ✅ plot.linestyle_dotted

### Currencies
- ✅ currency.AED
- ✅ currency.ARS
- ✅ currency.AUD
- ✅ currency.BDT
- ✅ currency.BHD
- ✅ currency.BRL
- ✅ currency.BTC
- ✅ currency.CAD
- ✅ currency.CHF
- ✅ currency.CLP
- ✅ currency.CNY
- ✅ currency.COP
- ✅ currency.CZK
- ✅ currency.DKK
- ✅ currency.EGP
- ✅ currency.ETH
- ✅ currency.EUR
- ✅ currency.GBP
- ✅ currency.HKD
- ✅ currency.HUF
- ✅ currency.IDR
- ✅ currency.ILS
- ✅ currency.INR
- ✅ currency.ISK
- ✅ currency.JPY
- ✅ currency.KES
- ✅ currency.KRW
- ✅ currency.KWD
- ✅ currency.LKR
- ✅ currency.MAD
- ✅ currency.MXN
- ✅ currency.MYR
- ✅ currency.NGN
- ✅ currency.NOK
- ✅ currency.NZD
- ✅ currency.PEN
- ✅ currency.PHP
- ✅ currency.PKR
- ✅ currency.PLN
- ✅ currency.QAR
- ✅ currency.RON
- ✅ currency.RSD
- ✅ currency.RUB
- ✅ currency.SAR
- ✅ currency.SEK
- ✅ currency.SGD
- ✅ currency.THB
- ✅ currency.TND
- ✅ currency.TRY
- ✅ currency.TWD
- ✅ currency.USD
- ✅ currency.USDT
- ✅ currency.VES
- ✅ currency.VND
- ✅ currency.ZAR

### Days of Week
- ✅ dayofweek.sunday
- ✅ dayofweek.monday
- ✅ dayofweek.tuesday
- ✅ dayofweek.wednesday
- ✅ dayofweek.thursday
- ✅ dayofweek.friday
- ✅ dayofweek.saturday

### Order
- ✅ order.ascending
- ✅ order.descending

### Adjustment
- ✅ adjustment.none
- ✅ adjustment.splits
- ✅ adjustment.dividends

### Backadjustment
- ✅ backadjustment.inherit
- ✅ backadjustment.on
- ✅ backadjustment.off

### Barmerge
- ✅ barmerge.gaps_on
- ✅ barmerge.gaps_off
- ✅ barmerge.lookahead_on
- ✅ barmerge.lookahead_off

### Format
- ✅ format.price
- ✅ format.volume
- ✅ format.percent
- ✅ format.inherit
- ✅ format.mintick

### Settlement as Close
- ✅ settlement_as_close.inherit
- ✅ settlement_as_close.on
- ✅ settlement_as_close.off

### Shape
- ✅ shape.arrowup
- ✅ shape.arrowdown
- ✅ shape.circle
- ✅ shape.cross
- ✅ shape.diamond
- ✅ shape.flag
- ✅ shape.labelup
- ✅ shape.labeldown
- ✅ shape.square
- ✅ shape.triangledown
- ✅ shape.triangleup
- ✅ shape.xcross

### Splits
- ✅ splits.denominator
- ✅ splits.numerator

### Strategy Commission Types
- ✅ strategy.commission.cash_per_contract
- ✅ strategy.commission.cash_per_order
- ✅ strategy.commission.percent

### Strategy Direction
- ✅ strategy.direction.all
- ✅ strategy.direction.long
- ✅ strategy.direction.short

### Strategy OCA Types
- ✅ strategy.oca.cancel
- ✅ strategy.oca.none
- ✅ strategy.oca.reduce

### Strategy Qty Types
- ✅ strategy.cash
- ✅ strategy.fixed
- ✅ strategy.percent_of_equity

### Strategy Risk
- ✅ strategy.risk.allow_entry_in
- ✅ strategy.risk.max_cons_loss_days
- ✅ strategy.risk.max_drawdown
- ✅ strategy.risk.max_intraday_filled_orders
- ✅ strategy.risk.max_intraday_loss
- ✅ strategy.risk.max_position_size

### True/False
- ✅ true
- ✅ false

## Functions

### Array Functions
- ✅ array.abs
- ✅ array.avg
- ✅ array.binary_search
- ❌ array.binary_search_leftmost
- ❌ array.binary_search_rightmost
- ✅ array.clear
- ✅ array.concat
- ✅ array.copy
- ✅ array.covariance
- ✅ array.every
- ✅ array.fill
- ✅ array.first
- ✅ array.from
- ✅ array.get
- ✅ array.includes
- ✅ array.indexof
- ✅ array.insert
- ✅ array.join
- ✅ array.last
- ✅ array.lastindexof
- ✅ array.max
- ✅ array.median
- ✅ array.min
- ✅ array.mode
- ✅ array.new_bool
- ✅ array.new_box
- ✅ array.new_color
- ✅ array.new_float
- ✅ array.new_int
- ✅ array.new_label
- ✅ array.new_line
- ❌ array.new_linefill
- ✅ array.new_string
- ✅ array.new_table
- ❌ array.new<type>
- ❌ array.percentile_linear_interpolation
- ❌ array.percentile_nearest_rank
- ❌ array.percentrank
- ✅ array.pop
- ✅ array.push
- ✅ array.range
- ✅ array.remove
- ✅ array.reverse
- ✅ array.set
- ✅ array.shift
- ✅ array.size
- ✅ array.slice
- ✅ array.some
- ✅ array.sort
- ❌ array.sort_indices
- ❌ array.standardize
- ❌ array.stdev
- ✅ array.sum
- ✅ array.unshift
- ❌ array.variance

### Math Functions
- ✅ math.abs
- ✅ math.acos
- ✅ math.asin
- ✅ math.atan
- ✅ math.avg
- ✅ math.ceil
- ✅ math.cos
- ✅ math.exp
- ✅ math.floor
- ✅ math.log
- ✅ math.log10
- ✅ math.max
- ✅ math.min
- ✅ math.pow
- ✅ math.random
- ✅ math.round
- ❌ math.round_to_mintick
- ✅ math.sign
- ✅ math.sin
- ✅ math.sqrt
- ✅ math.sum
- ✅ math.tan
- ✅ math.todegrees
- ✅ math.toradians

### String Functions
- ✅ str.contains
- ✅ str.endswith
- ✅ str.format
- ❌ str.format_time
- ✅ str.length
- ✅ str.lower
- ✅ str.match
- ✅ str.pos
- ✅ str.repeat
- ✅ str.replace
- ✅ str.replace_all
- ✅ str.split
- ✅ str.startswith
- ✅ str.substring
- ✅ str.tonumber
- ✅ str.tostring
- ✅ str.trim
- ✅ str.upper

### Technical Analysis Functions
- ✅ ta.alma
- ✅ ta.atr
- ✅ ta.adx
- ✅ ta.barssince
- ✅ ta.bb
- ✅ ta.bbw
- ✅ ta.cci
- ✅ ta.change
- ✅ ta.cmo
- ❌ ta.cog
- ✅ ta.correlation
- ✅ ta.cross
- ✅ ta.crossover
- ✅ ta.crossunder
- ✅ ta.cum
- ✅ ta.dev
- ❌ ta.dmi
- ✅ ta.ema
- ✅ ta.falling
- ✅ ta.highest
- ✅ ta.highestbars
- ✅ ta.hma
- ❌ ta.kc
- ❌ ta.kcw
- ❌ ta.linreg
- ✅ ta.lowest
- ✅ ta.lowestbars
- ✅ ta.macd
- ✅ ta.max
- ✅ ta.median
- ✅ ta.mfi
- ✅ ta.min
- ✅ ta.mode
- ✅ ta.mom
- ❌ ta.percentile_linear_interpolation
- ❌ ta.percentile_nearest_rank
- ❌ ta.percentrank
- ❌ ta.pivot_point_levels
- ❌ ta.pivothigh
- ❌ ta.pivotlow
- ✅ ta.range
- ❌ ta.rci
- ✅ ta.rising
- ✅ ta.rma
- ✅ ta.roc
- ✅ ta.rsi
- ✅ ta.sar
- ✅ ta.sma
- ✅ ta.stdev
- ✅ ta.stoch
- ❌ ta.supertrend
- ❌ ta.swma
- ❌ ta.tr
- ✅ ta.tsi
- ✅ ta.valuewhen
- ✅ ta.variance
- ✅ ta.vwap
- ✅ ta.vwma
- ✅ ta.wma
- ✅ ta.wpr
- ❌ ta.zigzag

### Plotting Functions
- ❌ plot
- ❌ plotarrow
- ❌ plotbar
- ❌ plotcandle
- ❌ plotchar
- ❌ plotshape
- ❌ fill
- ❌ bgcolor
- ❌ barcolor
- ❌ hline

### Input Functions
- ❌ input
- ❌ input.bool
- ❌ input.int
- ❌ input.float
- ❌ input.price
- ❌ input.string
- ❌ input.symbol
- ❌ input.session
- ❌ input.source
- ❌ input.time
- ❌ input.timeframe
- ❌ input.color
- ❌ input.enum

### Request Functions
- ❌ request.security
- ❌ request.security_lower_tf
- ❌ request.dividends
- ❌ request.earnings
- ❌ request.splits
- ❌ request.financial
- ❌ request.quandl
- ❌ request.economic
- ❌ request.currency_rate
- ❌ request.seed

### Drawing Functions
- ❌ line.new
- ❌ line.delete
- ❌ line.copy
- ❌ line.set_*
- ❌ line.get_*
- ❌ box.new
- ❌ box.delete
- ❌ box.copy
- ❌ box.set_*
- ❌ box.get_*
- ❌ label.new
- ❌ label.delete
- ❌ label.copy
- ❌ label.set_*
- ❌ label.get_*
- ❌ table.new
- ❌ table.delete
- ❌ table.cell
- ❌ table.cell_set_*
- ❌ table.clear
- ❌ table.merge_cells
- ❌ polyline.new
- ❌ polyline.delete
- ❌ linefill.new
- ❌ linefill.delete

### Strategy Functions
- ❌ strategy.entry
- ❌ strategy.exit
- ❌ strategy.close
- ❌ strategy.close_all
- ❌ strategy.cancel
- ❌ strategy.cancel_all
- ❌ strategy.order
- ❌ strategy.risk.*
- ❌ strategy.convert_to_*
- ❌ strategy.default_entry_qty
- ❌ strategy.closedtrades.*
- ❌ strategy.opentrades.*

### Indicator/Strategy Declaration
- ❌ indicator
- ❌ strategy
- ❌ library

### Utility Functions
- ❌ alert
- ❌ alertcondition
- ❌ log.error
- ❌ log.info
- ❌ log.warning
- ❌ runtime.error
- ❌ max_bars_back
- ❌ fixnan
- ❌ nz

### Type Conversion
- ❌ int
- ❌ float
- ❌ bool
- ❌ string
- ❌ color

### Ticker Functions
- ❌ ticker.new
- ❌ ticker.modify
- ❌ ticker.heikinashi
- ❌ ticker.kagi
- ❌ ticker.linebreak
- ❌ ticker.pointfigure
- ❌ ticker.renko
- ❌ ticker.standard
- ❌ ticker.inherit

### Time Functions
- ❌ time
- ❌ timestamp
- ❌ year
- ❌ month
- ❌ weekofyear
- ❌ dayofmonth
- ❌ dayofweek
- ❌ hour
- ❌ minute
- ❌ second
- ❌ time_close
- ❌ time_tradingday

### Chart Point Functions
- ❌ chart.point.new
- ❌ chart.point.from_index
- ❌ chart.point.from_time
- ❌ chart.point.now
- ❌ chart.point.copy

### Color Functions
- ❌ color.new
- ❌ color.r
- ❌ color.g
- ❌ color.b
- ❌ color.t
- ❌ color.rgb
- ❌ color.from_gradient

### Matrix Functions
- ❌ matrix.new<type>
- ❌ matrix.add_col
- ❌ matrix.add_row
- ❌ matrix.remove_col
- ❌ matrix.remove_row
- ❌ matrix.get
- ❌ matrix.set
- ❌ matrix.rows
- ❌ matrix.columns
- ❌ matrix.elements_count
- ❌ matrix.row
- ❌ matrix.col
- ❌ matrix.submatrix
- ❌ matrix.copy
- ❌ matrix.concat
- ❌ matrix.transpose
- ❌ matrix.inv
- ❌ matrix.pinv
- ❌ matrix.det
- ❌ matrix.rank
- ❌ matrix.trace
- ❌ matrix.eigenvalues
- ❌ matrix.eigenvectors
- ❌ matrix.pow
- ❌ matrix.mult
- ❌ matrix.add
- ❌ matrix.diff
- ❌ matrix.kron
- ❌ matrix.avg
- ❌ matrix.sum
- ❌ matrix.min
- ❌ matrix.max
- ❌ matrix.median
- ❌ matrix.mode
- ❌ matrix.fill
- ❌ matrix.reshape
- ❌ matrix.reverse
- ❌ matrix.sort
- ❌ matrix.swap_rows
- ❌ matrix.swap_columns
- ❌ matrix.is_square
- ❌ matrix.is_diagonal
- ❌ matrix.is_identity
- ❌ matrix.is_triangular
- ❌ matrix.is_symmetric
- ❌ matrix.is_antisymmetric
- ❌ matrix.is_zero
- ❌ matrix.is_stochastic
- ❌ matrix.is_binary
- ❌ matrix.is_antidiagonal

### Map Functions
- ❌ map.new<type,type>
- ❌ map.get
- ❌ map.put
- ❌ map.put_all
- ❌ map.remove
- ❌ map.clear
- ❌ map.contains
- ❌ map.keys
- ❌ map.values
- ❌ map.size
- ❌ map.copy

### Timeframe Functions
- ❌ timeframe.change
- ❌ timeframe.from_seconds
- ❌ timeframe.in_seconds

## Keywords

### Control Flow
- ✅ if
- ✅ else
- ✅ for
- ✅ for...in
- ✅ while
- ✅ switch
- ✅ break
- ✅ continue

### Declarations
- ✅ var
- ✅ varip
- ✅ const
- ✅ type
- ✅ method
- ✅ export
- ✅ import
- ✅ enum

### Logical
- ✅ and
- ✅ or
- ✅ not

### Special
- ✅ na
- ✅ true
- ✅ false

## Types

### Basic Types
- ✅ int
- ✅ float
- ✅ bool
- ✅ string
- ✅ color
- ✅ const
- ✅ input
- ✅ simple
- ✅ series

### Collection Types
- ❌ array
- ❌ matrix
- ❌ map

### Drawing Types
- ❌ line
- ❌ box
- ❌ label
- ❌ table
- ❌ polyline
- ❌ linefill
- ❌ chart.point

## Operators

### Arithmetic
- ✅ +
- ✅ -
- ✅ *
- ✅ /
- ✅ %
- ✅ +=
- ✅ -=
- ✅ *=
- ✅ /=
- ✅ %=

### Comparison
- ✅ ==
- ✅ !=
- ✅ <
- ✅ <=
- ✅ >
- ✅ >=

### Logical
- ✅ and
- ✅ or
- ✅ not

### Assignment
- ✅ =
- ✅ :=

### Conditional
- ✅ ?:

### History
- ✅ []

### Function
- ✅ =>

## Annotations

- ✅ @version
- ✅ @description
- ✅ @function
- ✅ @param
- ✅ @returns
- ✅ @type
- ✅ @field
- ✅ @variable
- ✅ @enum
- ✅ @strategy_alert_message

## Syntax Features

### Expressions
- ✅ Arithmetic expressions
- ✅ Logical expressions
- ✅ Comparison expressions
- ✅ Conditional expressions
- ✅ Function calls
- ✅ Variable access
- ✅ Array/tuple access
- ✅ Attribute access

### Statements
- ✅ Assignment
- ✅ Variable declaration
- ✅ Function declaration
- ✅ Type declaration
- ✅ If statements
- ✅ For loops
- ✅ While loops
- ✅ Switch statements
- ✅ Import statements
- ✅ Break/continue

### Literals
- ✅ Numbers (int, float, complex)
- ✅ Strings
- ✅ Booleans
- ✅ Colors
- ✅ Arrays
- ✅ Tuples

## Outstanding Tasks

1. Implement all built-in functions in evaluator/transformer
2. Add support for collection types (array, matrix, map)
3. Implement drawing object types and functions
4. Add strategy simulation capabilities
5. Implement request.* functions for external data
6. Add plotting and visualization support
7. Implement input system for interactive parameters
8. Add timeframe and security request handling
9. Implement technical analysis functions
10. Add math and string utility functions

## Current Implementation Status

- **Parser**: ~90% complete (basic syntax parsing)
- **Evaluator**: ~50% complete (expressions, functions, comparisons, conditionals)
- **Built-in Functions**: ~25% complete (70+ math/string/array/TA functions)
- **Types**: ~50% complete (basic types)
- **Collections**: ~60% complete (arrays/tuples basic support)
- **Drawing**: 0% complete
- **Strategy**: 0% complete

**Overall**: ~50-55% complete

### Recently Implemented (Evaluator)

#### Math Functions (11)
- math.max, math.min, math.abs, math.sqrt
- math.round, math.floor, math.ceil
- math.pow, math.log
- math.sin, math.cos, math.tan
- math.acos, math.asin, math.atan, math.exp, math.log10
- math.sign, math.sum, math.avg, math.todegrees, math.toradians

#### String Functions (14)

- str.length, str.upper, str.lower
- str.contains, str.startswith, str.substring
- str.endswith, str.repeat, str.replace, str.replace_all
- str.split, str.trim, str.tonumber, str.tostring

#### Array Functions (30)

- array.size, array.get, array.push, array.pop, array.slice
- array.abs, array.avg, array.concat, array.copy
- array.every, array.fill, array.first, array.from
- array.includes, array.indexof, array.insert, array.join
- array.last, array.lastindexof, array.max, array.min
- array.range, array.remove, array.reverse, array.set
- array.shift, array.some, array.sort, array.sum, array.unshift

#### Technical Analysis Functions (16)

- ta.alma (Arnaud Legoux Moving Average)
- ta.barssince
- ta.bbw (Bollinger Band Width)
- ta.cmo (Chande Momentum Oscillator)
- ta.correlation
- ta.cross
- ta.falling
- ta.highestbars
- ta.hma (Hull Moving Average)
- ta.lowestbars
- ta.rising
- ta.rma (Running Moving Average)
- ta.sar (Parabolic SAR)
- ta.tsi (True Strength Index)
- ta.vwap (Volume Weighted Average Price)
- ta.vwma (Volume Weighted Moving Average)

#### Utility Functions (6)

- na() - returns None
- nz() - null coalescing
- bool(), int(), float() - type conversions
- color.new() - color creation

#### Operators & Control Flow

- All arithmetic operators: +, -, *, /, %
- All comparison operators: ==, !=, <, <=, >, >=
- Boolean operators: and, or, not
- Conditional expressions: ? :
- Array indexing: [index]
- Attribute access: obj.attr
