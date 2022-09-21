import os
import pandas as pd
import pyparsing

from pynescript.ast.parser.helpers import parse
from pynescript.ast.parser.grammars import *

pyparsing.enable_all_warnings()


def check_file_sizes():
    scriptdir = "./pynescript/data/builtin_scripts"
    filenames = os.listdir(scriptdir)
    filesizes = []
    for filename in filenames:
        filepath = os.path.join(scriptdir, filename)
        with open(filepath, "rb") as f:
            filesize = len(f.read())
        filesizes.append((filename, filesize))
    data = pd.DataFrame.from_records(filesizes)
    print(data.sort_values(1).to_markdown())


def test_failing_parse():
    instring = """
//@version=5
indicator("Pivot Points Standard", "Pivots", overlay=true, max_lines_count=500, max_labels_count=500)

AUTO = "Auto"
DAILY = "Daily"
WEEKLY = "Weekly"
MONTHLY = "Monthly"
QUARTERLY = "Quarterly"
YEARLY = "Yearly"
BIYEARLY = "Biyearly"
TRIYEARLY = "Triyearly"
QUINQUENNIALLY = "Quinquennially"
DECENNIALLY = "Decennially"

TRADITIONAL = "Traditional"
FIBONACCI = "Fibonacci"
WOODIE = "Woodie"
CLASSIC = "Classic"
DEMARK = "DM"
CAMARILLA = "Camarilla"

kind = input.string(title="Type", defval="Traditional", options=[TRADITIONAL, FIBONACCI, WOODIE, CLASSIC, DEMARK, CAMARILLA])
pivot_time_frame = input.string(title="Pivots Timeframe", defval=AUTO, options=[AUTO, DAILY, WEEKLY, MONTHLY, QUARTERLY, YEARLY, BIYEARLY, TRIYEARLY, QUINQUENNIALLY, DECENNIALLY])
look_back = input.int(title="Number of Pivots Back", defval=15, minval=1, maxval=5000)
is_daily_based = input.bool(title="Use Daily-based Values", defval=true, tooltip="When this option is unchecked, Pivot Points will use intraday data while calculating on intraday charts. If Extended Hours are displayed on the chart, they will be taken into account during the pivot level calculation. If intraday OHLC values are different from daily-based values (normal for stocks), the pivot levels will also differ.")
show_labels = input.bool(title="Show Labels", defval=true, group="labels")
show_prices = input.bool(title="Show Prices", defval=true, group="labels")
position_labels = input.string("Left", "Labels Position", options=["Left", "Right"], group="labels")
line_width = input.int(title="Line Width", defval=1, minval=1, maxval=100, group="levels")

var DEF_COLOR = #FB8C00
var arr_time = array.new_int()
var p = array.new_float()
p_color = input.color(DEF_COLOR, "P‏  ‏  ‏", inline="P", group="levels")
p_show = input.bool(true, "", inline="P", group="levels")
var r1 = array.new_float()
var s1 = array.new_float()
s1_color = input.color(DEF_COLOR, "S1", inline="S1/R1" , group="levels")
s1_show = input.bool(true, "", inline="S1/R1", group="levels")
r1_color = input.color(DEF_COLOR, "‏  ‏  ‏  ‏  ‏  ‏  ‏  ‏R1", inline="S1/R1", group="levels")
r1_show = input.bool(true, "", inline="S1/R1", group="levels")
var r2 = array.new_float()
var s2 = array.new_float()
s2_color = input.color(DEF_COLOR, "S2", inline="S2/R2", group="levels")
s2_show = input.bool(true, "", inline="S2/R2", group="levels")
r2_color = input.color(DEF_COLOR, "‏  ‏  ‏  ‏  ‏  ‏  ‏  ‏R2", inline="S2/R2", group="levels")
r2_show = input.bool(true, "", inline="S2/R2", group="levels")
var r3 = array.new_float()
var s3 = array.new_float()
s3_color = input.color(DEF_COLOR, "S3", inline="S3/R3", group="levels")
s3_show = input.bool(true, "", inline="S3/R3", group="levels")
r3_color = input.color(DEF_COLOR, "‏  ‏  ‏  ‏  ‏  ‏  ‏  ‏R3", inline="S3/R3", group="levels")
r3_show = input.bool(true, "", inline="S3/R3", group="levels")
var r4 = array.new_float()
var s4 = array.new_float()
s4_color = input.color(DEF_COLOR, "S4", inline="S4/R4", group="levels")
s4_show = input.bool(true, "", inline="S4/R4", group="levels")
r4_color = input.color(DEF_COLOR, "‏  ‏  ‏  ‏  ‏  ‏  ‏  ‏R4", inline="S4/R4", group="levels")
r4_show = input.bool(true, "", inline="S4/R4", group="levels")
var r5 = array.new_float()
var s5 = array.new_float()
s5_color = input.color(DEF_COLOR, "S5", inline="S5/R5", group="levels")
s5_show = input.bool(true, "", inline="S5/R5", group="levels")
r5_color = input.color(DEF_COLOR, "‏  ‏  ‏  ‏  ‏  ‏  ‏  ‏R5", inline="S5/R5", group="levels")
r5_show = input.bool(true, "", inline="S5/R5", group="levels")
pivotX_open = float(na)
pivotX_open := nz(pivotX_open[1], open)
pivotX_high = float(na)
pivotX_high := nz(pivotX_high[1], high)
pivotX_low = float(na)
pivotX_low := nz(pivotX_low[1], low)
pivotX_prev_open = float(na)
pivotX_prev_open := nz(pivotX_prev_open[1])
pivotX_prev_high = float(na)
pivotX_prev_high := nz(pivotX_prev_high[1])
pivotX_prev_low = float(na)
pivotX_prev_low := nz(pivotX_prev_low[1])
pivotX_prev_close = float(na)
pivotX_prev_close := nz(pivotX_prev_close[1])

get_pivot_resolution() =>
    resolution = "M"
    if pivot_time_frame == AUTO
        if timeframe.isintraday
            resolution := timeframe.multiplier <= 15 ? "D" : "W"
        else if timeframe.isweekly or timeframe.ismonthly
            resolution := "12M"
    else if pivot_time_frame == DAILY
        resolution := "D"
    else if pivot_time_frame == WEEKLY
        resolution := "W"
    else if pivot_time_frame == MONTHLY
        resolution := "M"
    else if pivot_time_frame == QUARTERLY
        resolution := "3M"
    else if pivot_time_frame == YEARLY or pivot_time_frame == BIYEARLY or pivot_time_frame == TRIYEARLY or pivot_time_frame == QUINQUENNIALLY or pivot_time_frame == DECENNIALLY
        resolution := "12M"
    resolution

var lines = array.new_line()
var labels = array.new_label()

draw_line(i, pivot, col) =>
    if array.size(arr_time) > 1
        array.push(lines, line.new(array.get(arr_time, i), array.get(pivot, i), array.get(arr_time, i + 1), array.get(pivot, i), color=col, xloc=xloc.bar_time, width=line_width))

draw_label(i, y, txt, txt_color) =>
    if (show_labels or show_prices) and not na(y)
        display_text = (show_labels ? txt : "") + (show_prices ? str.format(" ({0})", math.round_to_mintick(y)) : "")
        label_style = position_labels == "Left" ? label.style_label_right : label.style_label_left
        x = position_labels == "Left" ? array.get(arr_time, i) : array.get(arr_time, i + 1)
        array.push(labels, label.new(x = x, y=y, text=display_text, textcolor=txt_color, style=label_style, color=#00000000, xloc=xloc.bar_time))

traditional() =>
    pivotX_Median = (pivotX_prev_high + pivotX_prev_low + pivotX_prev_close) / 3
    array.push(p, pivotX_Median)
    array.push(r1, pivotX_Median * 2 - pivotX_prev_low)
    array.push(s1, pivotX_Median * 2 - pivotX_prev_high)
    array.push(r2, pivotX_Median + 1 * (pivotX_prev_high - pivotX_prev_low))
    array.push(s2, pivotX_Median - 1 * (pivotX_prev_high - pivotX_prev_low))
    array.push(r3, pivotX_Median * 2 + (pivotX_prev_high - 2 * pivotX_prev_low))
    array.push(s3, pivotX_Median * 2 - (2 * pivotX_prev_high - pivotX_prev_low))
    array.push(r4, pivotX_Median * 3 + (pivotX_prev_high - 3 * pivotX_prev_low))
    array.push(s4, pivotX_Median * 3 - (3 * pivotX_prev_high - pivotX_prev_low))
    array.push(r5, pivotX_Median * 4 + (pivotX_prev_high - 4 * pivotX_prev_low))
    array.push(s5, pivotX_Median * 4 - (4 * pivotX_prev_high - pivotX_prev_low))

fibonacci() =>
    pivotX_Median = (pivotX_prev_high + pivotX_prev_low + pivotX_prev_close) / 3
    pivot_range = pivotX_prev_high - pivotX_prev_low
    array.push(p, pivotX_Median)
    array.push(r1, pivotX_Median + 0.382 * pivot_range)
    array.push(s1, pivotX_Median - 0.382 * pivot_range)
    array.push(r2, pivotX_Median + 0.618 * pivot_range)
    array.push(s2, pivotX_Median - 0.618 * pivot_range)
    array.push(r3, pivotX_Median + 1 * pivot_range)
    array.push(s3, pivotX_Median - 1 * pivot_range)

woodie() =>
    pivotX_Woodie_Median = (pivotX_prev_high + pivotX_prev_low + pivotX_open * 2)/4
    pivot_range = pivotX_prev_high - pivotX_prev_low
    array.push(p, pivotX_Woodie_Median)
    array.push(r1, pivotX_Woodie_Median * 2 - pivotX_prev_low)
    array.push(s1, pivotX_Woodie_Median * 2 - pivotX_prev_high)
    array.push(r2, pivotX_Woodie_Median + 1 * pivot_range)
    array.push(s2, pivotX_Woodie_Median - 1 * pivot_range)

    pivot_point_r3 = pivotX_prev_high + 2 * (pivotX_Woodie_Median - pivotX_prev_low)
    pivot_point_s3 = pivotX_prev_low - 2 * (pivotX_prev_high - pivotX_Woodie_Median)
    array.push(r3, pivot_point_r3)
    array.push(s3, pivot_point_s3)
    array.push(r4, pivot_point_r3 + pivot_range)
    array.push(s4, pivot_point_s3 - pivot_range)

classic() =>
    pivotX_Median = (pivotX_prev_high + pivotX_prev_low + pivotX_prev_close)/3
    pivot_range = pivotX_prev_high - pivotX_prev_low
    array.push(p, pivotX_Median)
    array.push(r1, pivotX_Median * 2 - pivotX_prev_low)
    array.push(s1, pivotX_Median * 2 - pivotX_prev_high)
    array.push(r2, pivotX_Median + 1 * pivot_range)
    array.push(s2, pivotX_Median - 1 * pivot_range)
    array.push(r3, pivotX_Median + 2 * pivot_range)
    array.push(s3, pivotX_Median - 2 * pivot_range)
    array.push(r4, pivotX_Median + 3 * pivot_range)
    array.push(s4, pivotX_Median - 3 * pivot_range)

demark() =>
    pivotX_Demark_X = pivotX_prev_high + pivotX_prev_low * 2 + pivotX_prev_close
    if pivotX_prev_close == pivotX_prev_open
        pivotX_Demark_X := pivotX_prev_high + pivotX_prev_low + pivotX_prev_close * 2
    if pivotX_prev_close > pivotX_prev_open
        pivotX_Demark_X := pivotX_prev_high * 2 + pivotX_prev_low + pivotX_prev_close
    array.push(p, pivotX_Demark_X / 4)
    array.push(r1, pivotX_Demark_X / 2 - pivotX_prev_low)
    array.push(s1, pivotX_Demark_X / 2 - pivotX_prev_high)

camarilla() =>
    pivotX_Median = (pivotX_prev_high + pivotX_prev_low + pivotX_prev_close) / 3
    pivot_range = pivotX_prev_high - pivotX_prev_low
    array.push(p, pivotX_Median)
    array.push(r1, pivotX_prev_close + pivot_range * 1.1 / 12.0)
    array.push(s1, pivotX_prev_close - pivot_range * 1.1 / 12.0)
    array.push(r2, pivotX_prev_close + pivot_range * 1.1 / 6.0)
    array.push(s2, pivotX_prev_close - pivot_range * 1.1 / 6.0)
    array.push(r3, pivotX_prev_close + pivot_range * 1.1 / 4.0)
    array.push(s3, pivotX_prev_close - pivot_range * 1.1 / 4.0)
    array.push(r4, pivotX_prev_close + pivot_range * 1.1 / 2.0)
    array.push(s4, pivotX_prev_close - pivot_range * 1.1 / 2.0)
    r5_val = pivotX_prev_high / pivotX_prev_low * pivotX_prev_close
	array.push(r5, r5_val)
	array.push(s5, 2 * pivotX_prev_close - r5_val)

calc_pivot() =>
    if kind == TRADITIONAL
        traditional()
    else if kind == FIBONACCI
        fibonacci()
    else if kind == WOODIE
        woodie()
    else if kind == CLASSIC
        classic()
    else if kind == DEMARK
        demark()
    else if kind == CAMARILLA
        camarilla()

resolution = get_pivot_resolution()

SIMPLE_DIVISOR = -1
custom_years_divisor = switch pivot_time_frame
	BIYEARLY => 2
	TRIYEARLY => 3
	QUINQUENNIALLY => 5
	DECENNIALLY => 10
	=> SIMPLE_DIVISOR

calc_high(prev, curr) =>
    if na(prev) or na(curr)
        nz(prev, nz(curr, na))
    else
        math.max(prev, curr)
    
calc_low(prev, curr) =>
    if not na(prev) and not na(curr)
        math.min(prev, curr)
    else
        nz(prev, nz(curr, na))

calc_OHLC_for_pivot(custom_years_divisor) =>
    if custom_years_divisor == SIMPLE_DIVISOR 
        [open, high, low, close, open[1], high[1], low[1], close[1], time[1], time_close]
    else
        var prev_sec_open = float(na)
        var prev_sec_high = float(na)
        var prev_sec_low = float(na)
        var prev_sec_close = float(na)
        var prev_sec_time = int(na)
        var curr_sec_open = float(na)
        var curr_sec_high = float(na)
        var curr_sec_low = float(na)
        var curr_sec_close = float(na)
        if year(time_close) % custom_years_divisor == 0
        	curr_sec_open := open
			curr_sec_high := high
			curr_sec_low := low
			curr_sec_close := close
            prev_sec_high := high[1]
            prev_sec_low := low[1]
            prev_sec_close := close[1]
            prev_sec_time := time[1]
            for i = 2 to custom_years_divisor
                prev_sec_open :=  nz(open[i], prev_sec_open)
                prev_sec_high := calc_high(prev_sec_high, high[i])
                prev_sec_low := calc_low(prev_sec_low, low[i])
                prev_sec_time := nz(time[i], prev_sec_time)
        [curr_sec_open, curr_sec_high, curr_sec_low, curr_sec_close, prev_sec_open, prev_sec_high, prev_sec_low, prev_sec_close, prev_sec_time, time_close]

[sec_open, sec_high, sec_low, sec_close, prev_sec_open, prev_sec_high, prev_sec_low, prev_sec_close, prev_sec_time, sec_time] = request.security(syminfo.tickerid, resolution, calc_OHLC_for_pivot(custom_years_divisor), lookahead = barmerge.lookahead_on)
sec_open_gaps_on = request.security(syminfo.tickerid, resolution, open, gaps = barmerge.gaps_on, lookahead = barmerge.lookahead_on)

is_change_years = custom_years_divisor > 0 and ta.change(time(resolution)) and year(time_close) % custom_years_divisor == 0

var is_change = false
var uses_current_bar = timeframe.isintraday and kind == WOODIE
var change_time = int(na)
is_time_change = (ta.change(time(resolution)) and custom_years_divisor == SIMPLE_DIVISOR) or is_change_years
if is_time_change
    change_time := time

var start_time = time
var was_last_premarket = false
var start_calculate_in_premarket = false

is_last_premarket = barstate.islast and session.ispremarket and time_close > sec_time and not was_last_premarket

if is_last_premarket
    was_last_premarket := true
    start_calculate_in_premarket := true
if session.ismarket
    was_last_premarket := false
    
without_time_change = barstate.islast and array.size(arr_time) == 0
is_can_calc_pivot = (not uses_current_bar and is_time_change and session.ismarket) or (ta.change(sec_open) and not start_calculate_in_premarket) or is_last_premarket or (uses_current_bar and not na(sec_open_gaps_on)) or without_time_change
enough_bars_for_calculate = prev_sec_time >= start_time or is_daily_based


if is_can_calc_pivot and enough_bars_for_calculate 
    if array.size(arr_time) == 0 and is_daily_based
        pivotX_prev_open := prev_sec_open[1]
        pivotX_prev_high := prev_sec_high[1]
        pivotX_prev_low := prev_sec_low[1]
        pivotX_prev_close := prev_sec_close[1]
        pivotX_open := sec_open[1]
        pivotX_high := sec_high[1]
        pivotX_low := sec_low[1]
        array.push(arr_time, start_time)
        calc_pivot()
    
    if is_daily_based
    	if is_last_premarket
            pivotX_prev_open := sec_open
            pivotX_prev_high := sec_high
            pivotX_prev_low := sec_low
            pivotX_prev_close := sec_close
            pivotX_open := open
            pivotX_high := high
            pivotX_low := low
        else
			pivotX_prev_open := prev_sec_open
			pivotX_prev_high := prev_sec_high
			pivotX_prev_low := prev_sec_low
			pivotX_prev_close := prev_sec_close
			pivotX_open := sec_open
			pivotX_high := sec_high
			pivotX_low := sec_low
    else
        pivotX_prev_high := pivotX_high
        pivotX_prev_low := pivotX_low
        pivotX_prev_open := pivotX_open
        pivotX_prev_close := close[1]
        pivotX_open := open
        pivotX_high := high
        pivotX_low := low

    if barstate.islast and not is_change and array.size(arr_time) > 0 and not without_time_change
        array.set(arr_time, array.size(arr_time) - 1, change_time)
    else if without_time_change
        array.push(arr_time, start_time)
    else
        array.push(arr_time, nz(change_time, time))

    calc_pivot()

    if array.size(arr_time) > look_back
        if array.size(arr_time) > 0
            array.shift(arr_time)
        if array.size(p) > 0 and p_show
            array.shift(p)
        if array.size(r1) > 0 and r1_show
            array.shift(r1)
        if array.size(s1) > 0 and s1_show
            array.shift(s1)
        if array.size(r2) > 0 and r2_show
            array.shift(r2)
        if array.size(s2) > 0 and s2_show
            array.shift(s2)
        if array.size(r3) > 0 and r3_show
            array.shift(r3)
        if array.size(s3) > 0 and s3_show
            array.shift(s3)
        if array.size(r4) > 0 and r4_show
            array.shift(r4)
        if array.size(s4) > 0 and s4_show
            array.shift(s4)
        if array.size(r5) > 0 and r5_show
            array.shift(r5)
        if array.size(s5) > 0 and s5_show
            array.shift(s5)
    is_change := true
else if not is_daily_based
    pivotX_high := math.max(pivotX_high, high)
    pivotX_low := math.min(pivotX_low, low)

if barstate.islast and not is_daily_based and array.size(arr_time) == 0 
    runtime.error("Not enough intraday data to calculate Pivot Points. Lower the Pivots Timeframe or turn on the 'Use Daily-based Values' option in the indicator settings.")

if barstate.islast and array.size(arr_time) > 0 and is_change
    is_change := false

    if custom_years_divisor > 0
        last_pivot_time = array.get(arr_time, array.size(arr_time) - 1)
        pivot_timeframe = str.tostring(12 * custom_years_divisor) + "M"
        estimate_pivot_time = last_pivot_time + timeframe.in_seconds(pivot_timeframe) * 1000
        array.push(arr_time, estimate_pivot_time)
    else
        array.push(arr_time, time_close(resolution))

    for i = 0 to array.size(lines) - 1
        if array.size(lines) > 0
            line.delete(array.shift(lines))
        if array.size(labels) > 0
            label.delete(array.shift(labels))

    for i = 0 to array.size(arr_time) - 2
        if array.size(p) > 0 and p_show
            draw_line(i, p, p_color)
            draw_label(i, array.get(p, i), "P", p_color)
        if array.size(r1) > 0 and r1_show
            draw_line(i, r1, r1_color)
            draw_label(i, array.get(r1, i), "R1", r1_color)
        if array.size(s1) > 0 and s1_show
            draw_line(i, s1, s1_color)
            draw_label(i, array.get(s1, i), "S1", s1_color)
        if array.size(r2) > 0 and r2_show
            draw_line(i, r2, r2_color)
            draw_label(i, array.get(r2, i), "R2", r2_color)
        if array.size(s2) > 0 and s2_show
            draw_line(i, s2, s2_color)
            draw_label(i, array.get(s2, i), "S2", s2_color)
        if array.size(r3) > 0 and r3_show
            draw_line(i, r3, r3_color)
            draw_label(i, array.get(r3, i), "R3", r3_color)
        if array.size(s3) > 0 and s3_show
            draw_line(i, s3, s3_color)
            draw_label(i, array.get(s3, i), "S3", s3_color)
        if array.size(r4) > 0 and r4_show
            draw_line(i, r4, r4_color)
            draw_label(i, array.get(r4, i), "R4", r4_color)
        if array.size(s4) > 0 and s4_show
            draw_line(i, s4, s4_color)
            draw_label(i, array.get(s4, i), "S4", s4_color)
        if array.size(r5) > 0 and r5_show
            draw_line(i, r5, r5_color)
            draw_label(i, array.get(r5, i), "R5", r5_color)
        if array.size(s5) > 0 and s5_show
            draw_line(i, s5, s5_color)
            draw_label(i, array.get(s5, i), "S5", s5_color)
    """

    res = parse(instring, parse_all=True)
    print(res)


if __name__ == "__main__":
    test_failing_parse()
