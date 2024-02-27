# Generated from C:/git/pynescript/src/pynescript/ast/grammar/antlr4/resource/PinescriptParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

if "." in __name__:
    from .PinescriptParserBase import PinescriptParserBase
else:
    from PinescriptParserBase import PinescriptParserBase

def serializedATN():
    return [
        4,1,63,817,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,72,
        7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,78,7,78,
        2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,84,2,85,
        7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,91,7,91,
        2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,97,2,98,
        7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,2,103,7,103,2,
        104,7,104,2,105,7,105,2,106,7,106,2,107,7,107,2,108,7,108,2,109,
        7,109,1,0,1,0,1,1,3,1,224,8,1,1,1,1,1,1,2,1,2,3,2,230,8,2,1,2,1,
        2,1,3,3,3,235,8,3,1,3,1,3,1,4,4,4,240,8,4,11,4,12,4,241,1,5,1,5,
        3,5,246,8,5,1,6,1,6,1,6,1,6,3,6,252,8,6,1,7,1,7,1,7,5,7,257,8,7,
        10,7,12,7,260,9,7,1,7,3,7,263,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,
        8,272,8,8,1,9,1,9,1,9,3,9,277,8,9,1,10,1,10,3,10,281,8,10,1,11,1,
        11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,15,3,15,300,8,15,1,15,3,15,303,8,15,1,15,1,15,1,15,3,15,
        308,8,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,5,16,317,8,16,10,16,
        12,16,320,9,16,1,16,3,16,323,8,16,1,17,3,17,326,8,17,1,17,1,17,1,
        17,3,17,331,8,17,1,18,3,18,334,8,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,19,4,19,344,8,19,11,19,12,19,345,1,20,1,20,1,20,1,20,3,20,
        352,8,20,1,20,1,20,1,21,1,21,1,21,1,21,3,21,360,8,21,1,22,1,22,1,
        23,1,23,1,24,1,24,3,24,368,8,24,1,25,1,25,1,25,1,25,1,25,1,26,1,
        26,1,26,1,26,3,26,379,8,26,1,27,1,27,3,27,383,8,27,1,28,1,28,1,28,
        1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,3,29,396,8,29,1,30,1,30,
        1,30,1,31,1,31,3,31,403,8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,3,32,413,8,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,34,
        1,34,3,34,425,8,34,1,35,1,35,1,35,1,35,1,36,1,36,3,36,433,8,36,1,
        36,1,36,1,36,1,36,1,36,1,37,4,37,441,8,37,11,37,12,37,442,1,37,3,
        37,446,8,37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,3,40,457,
        8,40,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,43,1,43,1,43,3,43,469,
        8,43,1,44,1,44,3,44,473,8,44,1,45,1,45,1,45,1,45,1,46,1,46,1,46,
        1,46,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,49,1,49,1,50,1,50,
        1,51,1,51,3,51,497,8,51,1,52,1,52,1,52,1,52,1,52,1,52,1,53,1,53,
        3,53,507,8,53,1,54,1,54,1,54,4,54,512,8,54,11,54,12,54,513,1,55,
        1,55,3,55,518,8,55,1,56,1,56,1,56,4,56,523,8,56,11,56,12,56,524,
        1,57,1,57,3,57,529,8,57,1,58,1,58,4,58,533,8,58,11,58,12,58,534,
        1,59,1,59,3,59,539,8,59,1,60,1,60,1,60,1,61,1,61,1,61,1,62,1,62,
        3,62,549,8,62,1,63,1,63,4,63,553,8,63,11,63,12,63,554,1,64,1,64,
        1,64,1,64,3,64,561,8,64,1,65,1,65,1,65,1,66,1,66,1,66,1,67,1,67,
        1,67,1,68,1,68,1,68,1,69,1,69,1,69,1,69,1,69,1,69,1,69,5,69,582,
        8,69,10,69,12,69,585,9,69,1,70,1,70,1,71,1,71,1,71,1,71,1,71,1,71,
        1,71,5,71,596,8,71,10,71,12,71,599,9,71,1,72,1,72,1,73,1,73,1,73,
        1,73,3,73,607,8,73,1,74,1,74,1,75,1,75,1,75,1,75,1,75,1,75,1,75,
        1,75,3,75,619,8,75,1,75,1,75,3,75,623,8,75,1,75,1,75,1,75,1,75,1,
        75,1,75,5,75,631,8,75,10,75,12,75,634,9,75,1,76,1,76,1,76,5,76,639,
        8,76,10,76,12,76,642,9,76,1,76,3,76,645,8,76,1,77,1,77,1,77,3,77,
        650,8,77,1,77,1,77,1,78,1,78,1,78,5,78,657,8,78,10,78,12,78,660,
        9,78,1,78,3,78,663,8,78,1,79,1,79,1,79,1,79,3,79,669,8,79,1,80,1,
        80,1,80,1,80,3,80,675,8,80,1,81,1,81,1,82,1,82,1,83,1,83,1,84,1,
        84,1,85,1,85,1,85,1,85,1,86,1,86,1,86,1,86,5,86,693,8,86,10,86,12,
        86,696,9,86,1,86,3,86,699,8,86,1,86,1,86,1,87,1,87,1,87,1,87,1,87,
        1,87,1,87,1,87,3,87,711,8,87,1,88,1,88,1,89,1,89,1,90,3,90,718,8,
        90,1,90,3,90,721,8,90,1,90,1,90,1,91,1,91,1,91,1,91,5,91,729,8,91,
        10,91,12,91,732,9,91,1,91,3,91,735,8,91,1,91,1,91,1,92,1,92,1,93,
        1,93,1,93,1,93,3,93,745,8,93,1,94,1,94,1,94,1,94,1,95,1,95,1,95,
        1,95,1,95,1,96,1,96,1,97,1,97,1,97,1,97,1,98,1,98,1,99,3,99,765,
        8,99,1,99,1,99,3,99,769,8,99,1,99,3,99,772,8,99,1,100,1,100,1,101,
        1,101,1,101,5,101,779,8,101,10,101,12,101,782,9,101,1,102,1,102,
        3,102,786,8,102,1,102,1,102,1,103,1,103,1,103,1,104,1,104,1,104,
        5,104,796,8,104,10,104,12,104,799,9,104,1,104,3,104,802,8,104,1,
        105,1,105,1,106,1,106,1,107,1,107,1,108,4,108,811,8,108,11,108,12,
        108,812,1,109,1,109,1,109,0,3,138,142,150,110,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,
        134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,
        166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,
        198,200,202,204,206,208,210,212,214,216,218,0,8,1,0,45,46,1,0,47,
        49,2,0,18,18,45,46,2,0,11,11,25,25,1,0,26,27,1,0,50,54,3,0,7,7,16,
        16,20,21,5,0,7,7,16,17,20,21,24,24,56,56,800,0,220,1,0,0,0,2,223,
        1,0,0,0,4,227,1,0,0,0,6,234,1,0,0,0,8,239,1,0,0,0,10,245,1,0,0,0,
        12,251,1,0,0,0,14,253,1,0,0,0,16,271,1,0,0,0,18,276,1,0,0,0,20,280,
        1,0,0,0,22,282,1,0,0,0,24,286,1,0,0,0,26,290,1,0,0,0,28,294,1,0,
        0,0,30,299,1,0,0,0,32,313,1,0,0,0,34,325,1,0,0,0,36,333,1,0,0,0,
        38,343,1,0,0,0,40,347,1,0,0,0,42,359,1,0,0,0,44,361,1,0,0,0,46,363,
        1,0,0,0,48,367,1,0,0,0,50,369,1,0,0,0,52,374,1,0,0,0,54,382,1,0,
        0,0,56,384,1,0,0,0,58,390,1,0,0,0,60,397,1,0,0,0,62,402,1,0,0,0,
        64,404,1,0,0,0,66,416,1,0,0,0,68,424,1,0,0,0,70,426,1,0,0,0,72,430,
        1,0,0,0,74,440,1,0,0,0,76,447,1,0,0,0,78,451,1,0,0,0,80,456,1,0,
        0,0,82,458,1,0,0,0,84,463,1,0,0,0,86,468,1,0,0,0,88,472,1,0,0,0,
        90,474,1,0,0,0,92,478,1,0,0,0,94,482,1,0,0,0,96,486,1,0,0,0,98,490,
        1,0,0,0,100,492,1,0,0,0,102,496,1,0,0,0,104,498,1,0,0,0,106,506,
        1,0,0,0,108,508,1,0,0,0,110,517,1,0,0,0,112,519,1,0,0,0,114,528,
        1,0,0,0,116,530,1,0,0,0,118,538,1,0,0,0,120,540,1,0,0,0,122,543,
        1,0,0,0,124,548,1,0,0,0,126,550,1,0,0,0,128,560,1,0,0,0,130,562,
        1,0,0,0,132,565,1,0,0,0,134,568,1,0,0,0,136,571,1,0,0,0,138,574,
        1,0,0,0,140,586,1,0,0,0,142,588,1,0,0,0,144,600,1,0,0,0,146,606,
        1,0,0,0,148,608,1,0,0,0,150,610,1,0,0,0,152,635,1,0,0,0,154,649,
        1,0,0,0,156,653,1,0,0,0,158,668,1,0,0,0,160,674,1,0,0,0,162,676,
        1,0,0,0,164,678,1,0,0,0,166,680,1,0,0,0,168,682,1,0,0,0,170,684,
        1,0,0,0,172,688,1,0,0,0,174,702,1,0,0,0,176,712,1,0,0,0,178,714,
        1,0,0,0,180,717,1,0,0,0,182,724,1,0,0,0,184,738,1,0,0,0,186,744,
        1,0,0,0,188,746,1,0,0,0,190,750,1,0,0,0,192,755,1,0,0,0,194,757,
        1,0,0,0,196,761,1,0,0,0,198,764,1,0,0,0,200,773,1,0,0,0,202,775,
        1,0,0,0,204,783,1,0,0,0,206,789,1,0,0,0,208,792,1,0,0,0,210,803,
        1,0,0,0,212,805,1,0,0,0,214,807,1,0,0,0,216,810,1,0,0,0,218,814,
        1,0,0,0,220,221,3,2,1,0,221,1,1,0,0,0,222,224,3,8,4,0,223,222,1,
        0,0,0,223,224,1,0,0,0,224,225,1,0,0,0,225,226,5,0,0,1,226,3,1,0,
        0,0,227,229,3,98,49,0,228,230,5,60,0,0,229,228,1,0,0,0,229,230,1,
        0,0,0,230,231,1,0,0,0,231,232,5,0,0,1,232,5,1,0,0,0,233,235,3,216,
        108,0,234,233,1,0,0,0,234,235,1,0,0,0,235,236,1,0,0,0,236,237,5,
        0,0,1,237,7,1,0,0,0,238,240,3,10,5,0,239,238,1,0,0,0,240,241,1,0,
        0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,9,1,0,0,0,243,246,3,12,6,
        0,244,246,3,14,7,0,245,243,1,0,0,0,245,244,1,0,0,0,246,11,1,0,0,
        0,247,252,3,18,9,0,248,252,3,30,15,0,249,252,3,36,18,0,250,252,3,
        44,22,0,251,247,1,0,0,0,251,248,1,0,0,0,251,249,1,0,0,0,251,250,
        1,0,0,0,252,13,1,0,0,0,253,258,3,16,8,0,254,255,5,42,0,0,255,257,
        3,16,8,0,256,254,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,258,259,
        1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,261,263,5,42,0,0,262,261,
        1,0,0,0,262,263,1,0,0,0,263,264,1,0,0,0,264,265,5,60,0,0,265,15,
        1,0,0,0,266,272,3,86,43,0,267,272,3,100,50,0,268,272,3,174,87,0,
        269,272,3,176,88,0,270,272,3,178,89,0,271,266,1,0,0,0,271,267,1,
        0,0,0,271,268,1,0,0,0,271,269,1,0,0,0,271,270,1,0,0,0,272,17,1,0,
        0,0,273,277,3,20,10,0,274,277,3,26,13,0,275,277,3,28,14,0,276,273,
        1,0,0,0,276,274,1,0,0,0,276,275,1,0,0,0,277,19,1,0,0,0,278,281,3,
        22,11,0,279,281,3,24,12,0,280,278,1,0,0,0,280,279,1,0,0,0,281,21,
        1,0,0,0,282,283,3,180,90,0,283,284,5,35,0,0,284,285,3,46,23,0,285,
        23,1,0,0,0,286,287,3,182,91,0,287,288,5,35,0,0,288,289,3,46,23,0,
        289,25,1,0,0,0,290,291,3,186,93,0,291,292,5,55,0,0,292,293,3,46,
        23,0,293,27,1,0,0,0,294,295,3,186,93,0,295,296,3,196,98,0,296,297,
        3,46,23,0,297,29,1,0,0,0,298,300,5,10,0,0,299,298,1,0,0,0,299,300,
        1,0,0,0,300,302,1,0,0,0,301,303,5,17,0,0,302,301,1,0,0,0,302,303,
        1,0,0,0,303,304,1,0,0,0,304,305,3,210,105,0,305,307,5,29,0,0,306,
        308,3,32,16,0,307,306,1,0,0,0,307,308,1,0,0,0,308,309,1,0,0,0,309,
        310,5,30,0,0,310,311,5,40,0,0,311,312,3,80,40,0,312,31,1,0,0,0,313,
        318,3,34,17,0,314,315,5,42,0,0,315,317,3,34,17,0,316,314,1,0,0,0,
        317,320,1,0,0,0,318,316,1,0,0,0,318,319,1,0,0,0,319,322,1,0,0,0,
        320,318,1,0,0,0,321,323,5,42,0,0,322,321,1,0,0,0,322,323,1,0,0,0,
        323,33,1,0,0,0,324,326,3,198,99,0,325,324,1,0,0,0,325,326,1,0,0,
        0,326,327,1,0,0,0,327,330,3,214,107,0,328,329,5,35,0,0,329,331,3,
        98,49,0,330,328,1,0,0,0,330,331,1,0,0,0,331,35,1,0,0,0,332,334,5,
        10,0,0,333,332,1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,336,5,
        24,0,0,336,337,3,210,105,0,337,338,5,60,0,0,338,339,5,1,0,0,339,
        340,3,38,19,0,340,341,5,2,0,0,341,37,1,0,0,0,342,344,3,40,20,0,343,
        342,1,0,0,0,344,345,1,0,0,0,345,343,1,0,0,0,345,346,1,0,0,0,346,
        39,1,0,0,0,347,348,3,198,99,0,348,351,3,214,107,0,349,350,5,35,0,
        0,350,352,3,98,49,0,351,349,1,0,0,0,351,352,1,0,0,0,352,353,1,0,
        0,0,353,354,5,60,0,0,354,41,1,0,0,0,355,360,3,48,24,0,356,360,3,
        62,31,0,357,360,3,70,35,0,358,360,3,72,36,0,359,355,1,0,0,0,359,
        356,1,0,0,0,359,357,1,0,0,0,359,358,1,0,0,0,360,43,1,0,0,0,361,362,
        3,42,21,0,362,45,1,0,0,0,363,364,3,42,21,0,364,47,1,0,0,0,365,368,
        3,50,25,0,366,368,3,52,26,0,367,365,1,0,0,0,367,366,1,0,0,0,368,
        49,1,0,0,0,369,370,5,13,0,0,370,371,3,98,49,0,371,372,3,80,40,0,
        372,373,3,54,27,0,373,51,1,0,0,0,374,375,5,13,0,0,375,376,3,98,49,
        0,376,378,3,80,40,0,377,379,3,60,30,0,378,377,1,0,0,0,378,379,1,
        0,0,0,379,53,1,0,0,0,380,383,3,56,28,0,381,383,3,58,29,0,382,380,
        1,0,0,0,382,381,1,0,0,0,383,55,1,0,0,0,384,385,5,9,0,0,385,386,5,
        13,0,0,386,387,3,98,49,0,387,388,3,80,40,0,388,389,3,54,27,0,389,
        57,1,0,0,0,390,391,5,9,0,0,391,392,5,13,0,0,392,393,3,98,49,0,393,
        395,3,80,40,0,394,396,3,60,30,0,395,394,1,0,0,0,395,396,1,0,0,0,
        396,59,1,0,0,0,397,398,5,9,0,0,398,399,3,80,40,0,399,61,1,0,0,0,
        400,403,3,64,32,0,401,403,3,66,33,0,402,400,1,0,0,0,402,401,1,0,
        0,0,403,63,1,0,0,0,404,405,5,12,0,0,405,406,3,68,34,0,406,407,5,
        35,0,0,407,408,3,98,49,0,408,409,5,23,0,0,409,412,3,98,49,0,410,
        411,5,6,0,0,411,413,3,98,49,0,412,410,1,0,0,0,412,413,1,0,0,0,413,
        414,1,0,0,0,414,415,3,80,40,0,415,65,1,0,0,0,416,417,5,12,0,0,417,
        418,3,68,34,0,418,419,5,15,0,0,419,420,3,98,49,0,420,421,3,80,40,
        0,421,67,1,0,0,0,422,425,3,214,107,0,423,425,3,182,91,0,424,422,
        1,0,0,0,424,423,1,0,0,0,425,69,1,0,0,0,426,427,5,28,0,0,427,428,
        3,98,49,0,428,429,3,80,40,0,429,71,1,0,0,0,430,432,5,22,0,0,431,
        433,3,98,49,0,432,431,1,0,0,0,432,433,1,0,0,0,433,434,1,0,0,0,434,
        435,5,60,0,0,435,436,5,1,0,0,436,437,3,74,37,0,437,438,5,2,0,0,438,
        73,1,0,0,0,439,441,3,76,38,0,440,439,1,0,0,0,441,442,1,0,0,0,442,
        440,1,0,0,0,442,443,1,0,0,0,443,445,1,0,0,0,444,446,3,78,39,0,445,
        444,1,0,0,0,445,446,1,0,0,0,446,75,1,0,0,0,447,448,3,98,49,0,448,
        449,5,40,0,0,449,450,3,80,40,0,450,77,1,0,0,0,451,452,5,40,0,0,452,
        453,3,80,40,0,453,79,1,0,0,0,454,457,3,82,41,0,455,457,3,84,42,0,
        456,454,1,0,0,0,456,455,1,0,0,0,457,81,1,0,0,0,458,459,5,60,0,0,
        459,460,5,1,0,0,460,461,3,8,4,0,461,462,5,2,0,0,462,83,1,0,0,0,463,
        464,3,10,5,0,464,85,1,0,0,0,465,469,3,88,44,0,466,469,3,94,47,0,
        467,469,3,96,48,0,468,465,1,0,0,0,468,466,1,0,0,0,468,467,1,0,0,
        0,469,87,1,0,0,0,470,473,3,90,45,0,471,473,3,92,46,0,472,470,1,0,
        0,0,472,471,1,0,0,0,473,89,1,0,0,0,474,475,3,180,90,0,475,476,5,
        35,0,0,476,477,3,98,49,0,477,91,1,0,0,0,478,479,3,182,91,0,479,480,
        5,35,0,0,480,481,3,98,49,0,481,93,1,0,0,0,482,483,3,186,93,0,483,
        484,5,55,0,0,484,485,3,98,49,0,485,95,1,0,0,0,486,487,3,186,93,0,
        487,488,3,196,98,0,488,489,3,98,49,0,489,97,1,0,0,0,490,491,3,102,
        51,0,491,99,1,0,0,0,492,493,3,98,49,0,493,101,1,0,0,0,494,497,3,
        104,52,0,495,497,3,106,53,0,496,494,1,0,0,0,496,495,1,0,0,0,497,
        103,1,0,0,0,498,499,3,106,53,0,499,500,5,44,0,0,500,501,3,98,49,
        0,501,502,5,43,0,0,502,503,3,98,49,0,503,105,1,0,0,0,504,507,3,108,
        54,0,505,507,3,110,55,0,506,504,1,0,0,0,506,505,1,0,0,0,507,107,
        1,0,0,0,508,511,3,110,55,0,509,510,5,19,0,0,510,512,3,110,55,0,511,
        509,1,0,0,0,512,513,1,0,0,0,513,511,1,0,0,0,513,514,1,0,0,0,514,
        109,1,0,0,0,515,518,3,112,56,0,516,518,3,114,57,0,517,515,1,0,0,
        0,517,516,1,0,0,0,518,111,1,0,0,0,519,522,3,114,57,0,520,521,5,3,
        0,0,521,523,3,114,57,0,522,520,1,0,0,0,523,524,1,0,0,0,524,522,1,
        0,0,0,524,525,1,0,0,0,525,113,1,0,0,0,526,529,3,116,58,0,527,529,
        3,124,62,0,528,526,1,0,0,0,528,527,1,0,0,0,529,115,1,0,0,0,530,532,
        3,124,62,0,531,533,3,118,59,0,532,531,1,0,0,0,533,534,1,0,0,0,534,
        532,1,0,0,0,534,535,1,0,0,0,535,117,1,0,0,0,536,539,3,120,60,0,537,
        539,3,122,61,0,538,536,1,0,0,0,538,537,1,0,0,0,539,119,1,0,0,0,540,
        541,5,36,0,0,541,542,3,124,62,0,542,121,1,0,0,0,543,544,5,37,0,0,
        544,545,3,124,62,0,545,123,1,0,0,0,546,549,3,126,63,0,547,549,3,
        138,69,0,548,546,1,0,0,0,548,547,1,0,0,0,549,125,1,0,0,0,550,552,
        3,138,69,0,551,553,3,128,64,0,552,551,1,0,0,0,553,554,1,0,0,0,554,
        552,1,0,0,0,554,555,1,0,0,0,555,127,1,0,0,0,556,561,3,130,65,0,557,
        561,3,132,66,0,558,561,3,134,67,0,559,561,3,136,68,0,560,556,1,0,
        0,0,560,557,1,0,0,0,560,558,1,0,0,0,560,559,1,0,0,0,561,129,1,0,
        0,0,562,563,5,38,0,0,563,564,3,138,69,0,564,131,1,0,0,0,565,566,
        5,33,0,0,566,567,3,138,69,0,567,133,1,0,0,0,568,569,5,39,0,0,569,
        570,3,138,69,0,570,135,1,0,0,0,571,572,5,34,0,0,572,573,3,138,69,
        0,573,137,1,0,0,0,574,575,6,69,-1,0,575,576,3,142,71,0,576,583,1,
        0,0,0,577,578,10,2,0,0,578,579,3,140,70,0,579,580,3,142,71,0,580,
        582,1,0,0,0,581,577,1,0,0,0,582,585,1,0,0,0,583,581,1,0,0,0,583,
        584,1,0,0,0,584,139,1,0,0,0,585,583,1,0,0,0,586,587,7,0,0,0,587,
        141,1,0,0,0,588,589,6,71,-1,0,589,590,3,146,73,0,590,597,1,0,0,0,
        591,592,10,2,0,0,592,593,3,144,72,0,593,594,3,146,73,0,594,596,1,
        0,0,0,595,591,1,0,0,0,596,599,1,0,0,0,597,595,1,0,0,0,597,598,1,
        0,0,0,598,143,1,0,0,0,599,597,1,0,0,0,600,601,7,1,0,0,601,145,1,
        0,0,0,602,603,3,148,74,0,603,604,3,146,73,0,604,607,1,0,0,0,605,
        607,3,150,75,0,606,602,1,0,0,0,606,605,1,0,0,0,607,147,1,0,0,0,608,
        609,7,2,0,0,609,149,1,0,0,0,610,611,6,75,-1,0,611,612,3,158,79,0,
        612,632,1,0,0,0,613,614,10,4,0,0,614,615,5,41,0,0,615,631,3,212,
        106,0,616,618,10,3,0,0,617,619,3,204,102,0,618,617,1,0,0,0,618,619,
        1,0,0,0,619,620,1,0,0,0,620,622,5,29,0,0,621,623,3,152,76,0,622,
        621,1,0,0,0,622,623,1,0,0,0,623,624,1,0,0,0,624,631,5,30,0,0,625,
        626,10,2,0,0,626,627,5,31,0,0,627,628,3,156,78,0,628,629,5,32,0,
        0,629,631,1,0,0,0,630,613,1,0,0,0,630,616,1,0,0,0,630,625,1,0,0,
        0,631,634,1,0,0,0,632,630,1,0,0,0,632,633,1,0,0,0,633,151,1,0,0,
        0,634,632,1,0,0,0,635,640,3,154,77,0,636,637,5,42,0,0,637,639,3,
        154,77,0,638,636,1,0,0,0,639,642,1,0,0,0,640,638,1,0,0,0,640,641,
        1,0,0,0,641,644,1,0,0,0,642,640,1,0,0,0,643,645,5,42,0,0,644,643,
        1,0,0,0,644,645,1,0,0,0,645,153,1,0,0,0,646,647,3,214,107,0,647,
        648,5,35,0,0,648,650,1,0,0,0,649,646,1,0,0,0,649,650,1,0,0,0,650,
        651,1,0,0,0,651,652,3,98,49,0,652,155,1,0,0,0,653,658,3,98,49,0,
        654,655,5,42,0,0,655,657,3,98,49,0,656,654,1,0,0,0,657,660,1,0,0,
        0,658,656,1,0,0,0,658,659,1,0,0,0,659,662,1,0,0,0,660,658,1,0,0,
        0,661,663,5,42,0,0,662,661,1,0,0,0,662,663,1,0,0,0,663,157,1,0,0,
        0,664,669,3,212,106,0,665,669,3,160,80,0,666,669,3,170,85,0,667,
        669,3,172,86,0,668,664,1,0,0,0,668,665,1,0,0,0,668,666,1,0,0,0,668,
        667,1,0,0,0,669,159,1,0,0,0,670,675,3,162,81,0,671,675,3,164,82,
        0,672,675,3,166,83,0,673,675,3,168,84,0,674,670,1,0,0,0,674,671,
        1,0,0,0,674,672,1,0,0,0,674,673,1,0,0,0,675,161,1,0,0,0,676,677,
        5,57,0,0,677,163,1,0,0,0,678,679,5,58,0,0,679,165,1,0,0,0,680,681,
        7,3,0,0,681,167,1,0,0,0,682,683,5,59,0,0,683,169,1,0,0,0,684,685,
        5,29,0,0,685,686,3,98,49,0,686,687,5,30,0,0,687,171,1,0,0,0,688,
        689,5,31,0,0,689,694,3,98,49,0,690,691,5,42,0,0,691,693,3,98,49,
        0,692,690,1,0,0,0,693,696,1,0,0,0,694,692,1,0,0,0,694,695,1,0,0,
        0,695,698,1,0,0,0,696,694,1,0,0,0,697,699,5,42,0,0,698,697,1,0,0,
        0,698,699,1,0,0,0,699,700,1,0,0,0,700,701,5,32,0,0,701,173,1,0,0,
        0,702,703,5,14,0,0,703,704,3,210,105,0,704,705,5,48,0,0,705,706,
        3,210,105,0,706,707,5,48,0,0,707,710,3,162,81,0,708,709,5,4,0,0,
        709,711,3,210,105,0,710,708,1,0,0,0,710,711,1,0,0,0,711,175,1,0,
        0,0,712,713,5,5,0,0,713,177,1,0,0,0,714,715,5,8,0,0,715,179,1,0,
        0,0,716,718,3,184,92,0,717,716,1,0,0,0,717,718,1,0,0,0,718,720,1,
        0,0,0,719,721,3,198,99,0,720,719,1,0,0,0,720,721,1,0,0,0,721,722,
        1,0,0,0,722,723,3,214,107,0,723,181,1,0,0,0,724,725,5,31,0,0,725,
        730,3,214,107,0,726,727,5,42,0,0,727,729,3,214,107,0,728,726,1,0,
        0,0,729,732,1,0,0,0,730,728,1,0,0,0,730,731,1,0,0,0,731,734,1,0,
        0,0,732,730,1,0,0,0,733,735,5,42,0,0,734,733,1,0,0,0,734,735,1,0,
        0,0,735,736,1,0,0,0,736,737,5,32,0,0,737,183,1,0,0,0,738,739,7,4,
        0,0,739,185,1,0,0,0,740,745,3,188,94,0,741,745,3,190,95,0,742,745,
        3,192,96,0,743,745,3,194,97,0,744,740,1,0,0,0,744,741,1,0,0,0,744,
        742,1,0,0,0,744,743,1,0,0,0,745,187,1,0,0,0,746,747,3,150,75,0,747,
        748,5,41,0,0,748,749,3,214,107,0,749,189,1,0,0,0,750,751,3,150,75,
        0,751,752,5,31,0,0,752,753,3,156,78,0,753,754,5,32,0,0,754,191,1,
        0,0,0,755,756,3,214,107,0,756,193,1,0,0,0,757,758,5,29,0,0,758,759,
        3,186,93,0,759,760,5,30,0,0,760,195,1,0,0,0,761,762,7,5,0,0,762,
        197,1,0,0,0,763,765,3,200,100,0,764,763,1,0,0,0,764,765,1,0,0,0,
        765,766,1,0,0,0,766,768,3,202,101,0,767,769,3,204,102,0,768,767,
        1,0,0,0,768,769,1,0,0,0,769,771,1,0,0,0,770,772,3,206,103,0,771,
        770,1,0,0,0,771,772,1,0,0,0,772,199,1,0,0,0,773,774,7,6,0,0,774,
        201,1,0,0,0,775,780,3,212,106,0,776,777,5,41,0,0,777,779,3,212,106,
        0,778,776,1,0,0,0,779,782,1,0,0,0,780,778,1,0,0,0,780,781,1,0,0,
        0,781,203,1,0,0,0,782,780,1,0,0,0,783,785,5,33,0,0,784,786,3,208,
        104,0,785,784,1,0,0,0,785,786,1,0,0,0,786,787,1,0,0,0,787,788,5,
        34,0,0,788,205,1,0,0,0,789,790,5,31,0,0,790,791,5,32,0,0,791,207,
        1,0,0,0,792,797,3,198,99,0,793,794,5,42,0,0,794,796,3,198,99,0,795,
        793,1,0,0,0,796,799,1,0,0,0,797,795,1,0,0,0,797,798,1,0,0,0,798,
        801,1,0,0,0,799,797,1,0,0,0,800,802,5,42,0,0,801,800,1,0,0,0,801,
        802,1,0,0,0,802,209,1,0,0,0,803,804,7,7,0,0,804,211,1,0,0,0,805,
        806,3,210,105,0,806,213,1,0,0,0,807,808,3,210,105,0,808,215,1,0,
        0,0,809,811,3,218,109,0,810,809,1,0,0,0,811,812,1,0,0,0,812,810,
        1,0,0,0,812,813,1,0,0,0,813,217,1,0,0,0,814,815,5,62,0,0,815,219,
        1,0,0,0,76,223,229,234,241,245,251,258,262,271,276,280,299,302,307,
        318,322,325,330,333,345,351,359,367,378,382,395,402,412,424,432,
        442,445,456,468,472,496,506,513,517,524,528,534,538,548,554,560,
        583,597,606,618,622,630,632,640,644,649,658,662,668,674,694,698,
        710,717,720,730,734,744,764,768,771,780,785,797,801,812
    ]

class PinescriptParser ( PinescriptParserBase ):

    grammarFileName = "PinescriptParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'and'", "'as'", 
                     "'break'", "'by'", "'const'", "'continue'", "'else'", 
                     "'export'", "'false'", "'for'", "'if'", "'import'", 
                     "'in'", "'input'", "'method'", "'not'", "'or'", "'series'", 
                     "'simple'", "'switch'", "'to'", "'type'", "'true'", 
                     "'var'", "'varip'", "'while'", "'('", "')'", "'['", 
                     "']'", "'<'", "'>'", "'='", "'=='", "'!='", "'<='", 
                     "'>='", "'=>'", "'.'", "','", "':'", "'?'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "':='" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "AND", "AS", "BREAK", 
                      "BY", "CONST", "CONTINUE", "ELSE", "EXPORT", "FALSE", 
                      "FOR", "IF", "IMPORT", "IN", "INPUT", "METHOD", "NOT", 
                      "OR", "SERIES", "SIMPLE", "SWITCH", "TO", "TYPE", 
                      "TRUE", "VAR", "VARIP", "WHILE", "LPAR", "RPAR", "LSQB", 
                      "RSQB", "LESS", "GREATER", "EQUAL", "EQEQUAL", "NOTEQUAL", 
                      "LESSEQUAL", "GREATEREQUAL", "RARROW", "DOT", "COMMA", 
                      "COLON", "QUESTION", "PLUS", "MINUS", "STAR", "SLASH", 
                      "PERCENT", "PLUSEQUAL", "MINEQUAL", "STAREQUAL", "SLASHEQUAL", 
                      "PERCENTEQUAL", "COLONEQUAL", "NAME", "NUMBER", "STRING", 
                      "COLOR", "NEWLINE", "WS", "COMMENT", "ERROR_TOKEN" ]

    RULE_start = 0
    RULE_start_script = 1
    RULE_start_expression = 2
    RULE_start_comments = 3
    RULE_statements = 4
    RULE_statement = 5
    RULE_compound_statement = 6
    RULE_simple_statements = 7
    RULE_simple_statement = 8
    RULE_compound_assignment = 9
    RULE_compound_variable_initialization = 10
    RULE_compound_name_initialization = 11
    RULE_compound_tuple_initialization = 12
    RULE_compound_reassignment = 13
    RULE_compound_augassignment = 14
    RULE_function_declaration = 15
    RULE_parameter_list = 16
    RULE_parameter_definition = 17
    RULE_type_declaration = 18
    RULE_field_definitions = 19
    RULE_field_definition = 20
    RULE_structure = 21
    RULE_structure_statement = 22
    RULE_structure_expression = 23
    RULE_if_structure = 24
    RULE_if_structure_elif = 25
    RULE_if_structure_else = 26
    RULE_elif_structure = 27
    RULE_elif_structure_elif = 28
    RULE_elif_structure_else = 29
    RULE_else_block = 30
    RULE_for_structure = 31
    RULE_for_structure_to = 32
    RULE_for_structure_in = 33
    RULE_for_iterator = 34
    RULE_while_structure = 35
    RULE_switch_structure = 36
    RULE_switch_cases = 37
    RULE_switch_pattern_case = 38
    RULE_switch_default_case = 39
    RULE_local_block = 40
    RULE_indented_local_block = 41
    RULE_inline_local_block = 42
    RULE_simple_assignment = 43
    RULE_simple_variable_initialization = 44
    RULE_simple_name_initialization = 45
    RULE_simple_tuple_initialization = 46
    RULE_simple_reassignment = 47
    RULE_simple_augassignment = 48
    RULE_expression = 49
    RULE_expression_statement = 50
    RULE_conditional_expression = 51
    RULE_conditional_expression_rule = 52
    RULE_disjunction_expression = 53
    RULE_disjunction_expression_rule = 54
    RULE_conjunction_expression = 55
    RULE_conjunction_expression_rule = 56
    RULE_equality_expression = 57
    RULE_equality_expression_rule = 58
    RULE_equality_trailing_pair = 59
    RULE_equal_trailing_pair = 60
    RULE_not_equal_trailing_pair = 61
    RULE_inequality_expression = 62
    RULE_inequality_expression_rule = 63
    RULE_inequality_trailing_pair = 64
    RULE_less_than_equal_trailing_pair = 65
    RULE_less_than_trailing_pair = 66
    RULE_greater_than_equal_trailing_pair = 67
    RULE_greater_than_trailing_pair = 68
    RULE_additive_expression = 69
    RULE_additive_op = 70
    RULE_multiplicative_expression = 71
    RULE_multiplicative_op = 72
    RULE_unary_expression = 73
    RULE_unary_op = 74
    RULE_primary_expression = 75
    RULE_argument_list = 76
    RULE_argument_definition = 77
    RULE_subscript_slice = 78
    RULE_atomic_expression = 79
    RULE_literal_expression = 80
    RULE_literal_number = 81
    RULE_literal_string = 82
    RULE_literal_bool = 83
    RULE_literal_color = 84
    RULE_grouped_expression = 85
    RULE_tuple_expression = 86
    RULE_import_statement = 87
    RULE_break_statement = 88
    RULE_continue_statement = 89
    RULE_variable_declaration = 90
    RULE_tuple_declaration = 91
    RULE_declaration_mode = 92
    RULE_assignment_target = 93
    RULE_assignment_target_attribute = 94
    RULE_assignment_target_subscript = 95
    RULE_assignment_target_name = 96
    RULE_assignment_target_group = 97
    RULE_augassign_op = 98
    RULE_type_specification = 99
    RULE_type_qualifier = 100
    RULE_attributed_type_name = 101
    RULE_template_spec_suffix = 102
    RULE_array_type_suffix = 103
    RULE_type_argument_list = 104
    RULE_name = 105
    RULE_name_load = 106
    RULE_name_store = 107
    RULE_comments = 108
    RULE_comment = 109

    ruleNames =  [ "start", "start_script", "start_expression", "start_comments", 
                   "statements", "statement", "compound_statement", "simple_statements", 
                   "simple_statement", "compound_assignment", "compound_variable_initialization", 
                   "compound_name_initialization", "compound_tuple_initialization", 
                   "compound_reassignment", "compound_augassignment", "function_declaration", 
                   "parameter_list", "parameter_definition", "type_declaration", 
                   "field_definitions", "field_definition", "structure", 
                   "structure_statement", "structure_expression", "if_structure", 
                   "if_structure_elif", "if_structure_else", "elif_structure", 
                   "elif_structure_elif", "elif_structure_else", "else_block", 
                   "for_structure", "for_structure_to", "for_structure_in", 
                   "for_iterator", "while_structure", "switch_structure", 
                   "switch_cases", "switch_pattern_case", "switch_default_case", 
                   "local_block", "indented_local_block", "inline_local_block", 
                   "simple_assignment", "simple_variable_initialization", 
                   "simple_name_initialization", "simple_tuple_initialization", 
                   "simple_reassignment", "simple_augassignment", "expression", 
                   "expression_statement", "conditional_expression", "conditional_expression_rule", 
                   "disjunction_expression", "disjunction_expression_rule", 
                   "conjunction_expression", "conjunction_expression_rule", 
                   "equality_expression", "equality_expression_rule", "equality_trailing_pair", 
                   "equal_trailing_pair", "not_equal_trailing_pair", "inequality_expression", 
                   "inequality_expression_rule", "inequality_trailing_pair", 
                   "less_than_equal_trailing_pair", "less_than_trailing_pair", 
                   "greater_than_equal_trailing_pair", "greater_than_trailing_pair", 
                   "additive_expression", "additive_op", "multiplicative_expression", 
                   "multiplicative_op", "unary_expression", "unary_op", 
                   "primary_expression", "argument_list", "argument_definition", 
                   "subscript_slice", "atomic_expression", "literal_expression", 
                   "literal_number", "literal_string", "literal_bool", "literal_color", 
                   "grouped_expression", "tuple_expression", "import_statement", 
                   "break_statement", "continue_statement", "variable_declaration", 
                   "tuple_declaration", "declaration_mode", "assignment_target", 
                   "assignment_target_attribute", "assignment_target_subscript", 
                   "assignment_target_name", "assignment_target_group", 
                   "augassign_op", "type_specification", "type_qualifier", 
                   "attributed_type_name", "template_spec_suffix", "array_type_suffix", 
                   "type_argument_list", "name", "name_load", "name_store", 
                   "comments", "comment" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    AND=3
    AS=4
    BREAK=5
    BY=6
    CONST=7
    CONTINUE=8
    ELSE=9
    EXPORT=10
    FALSE=11
    FOR=12
    IF=13
    IMPORT=14
    IN=15
    INPUT=16
    METHOD=17
    NOT=18
    OR=19
    SERIES=20
    SIMPLE=21
    SWITCH=22
    TO=23
    TYPE=24
    TRUE=25
    VAR=26
    VARIP=27
    WHILE=28
    LPAR=29
    RPAR=30
    LSQB=31
    RSQB=32
    LESS=33
    GREATER=34
    EQUAL=35
    EQEQUAL=36
    NOTEQUAL=37
    LESSEQUAL=38
    GREATEREQUAL=39
    RARROW=40
    DOT=41
    COMMA=42
    COLON=43
    QUESTION=44
    PLUS=45
    MINUS=46
    STAR=47
    SLASH=48
    PERCENT=49
    PLUSEQUAL=50
    MINEQUAL=51
    STAREQUAL=52
    SLASHEQUAL=53
    PERCENTEQUAL=54
    COLONEQUAL=55
    NAME=56
    NUMBER=57
    STRING=58
    COLOR=59
    NEWLINE=60
    WS=61
    COMMENT=62
    ERROR_TOKEN=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start_script(self):
            return self.getTypedRuleContext(PinescriptParser.Start_scriptContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = PinescriptParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.start_script()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_scriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PinescriptParser.EOF, 0)

        def statements(self):
            return self.getTypedRuleContext(PinescriptParser.StatementsContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_start_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_script" ):
                listener.enterStart_script(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_script" ):
                listener.exitStart_script(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_script" ):
                return visitor.visitStart_script(self)
            else:
                return visitor.visitChildren(self)




    def start_script(self):

        localctx = PinescriptParser.Start_scriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080969466897464736) != 0):
                self.state = 222
                self.statements()


            self.state = 225
            self.match(PinescriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(PinescriptParser.EOF, 0)

        def NEWLINE(self):
            return self.getToken(PinescriptParser.NEWLINE, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_start_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_expression" ):
                listener.enterStart_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_expression" ):
                listener.exitStart_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_expression" ):
                return visitor.visitStart_expression(self)
            else:
                return visitor.visitChildren(self)




    def start_expression(self):

        localctx = PinescriptParser.Start_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_start_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.expression()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==60:
                self.state = 228
                self.match(PinescriptParser.NEWLINE)


            self.state = 231
            self.match(PinescriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_commentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PinescriptParser.EOF, 0)

        def comments(self):
            return self.getTypedRuleContext(PinescriptParser.CommentsContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_start_comments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_comments" ):
                listener.enterStart_comments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_comments" ):
                listener.exitStart_comments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_comments" ):
                return visitor.visitStart_comments(self)
            else:
                return visitor.visitChildren(self)




    def start_comments(self):

        localctx = PinescriptParser.Start_commentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_start_comments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 233
                self.comments()


            self.state = 236
            self.match(PinescriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.StatementContext,i)


        def getRuleIndex(self):
            return PinescriptParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = PinescriptParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 238
                self.statement()
                self.state = 241 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1080969466897464736) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compound_statement(self):
            return self.getTypedRuleContext(PinescriptParser.Compound_statementContext,0)


        def simple_statements(self):
            return self.getTypedRuleContext(PinescriptParser.Simple_statementsContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PinescriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.compound_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.simple_statements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compound_assignment(self):
            return self.getTypedRuleContext(PinescriptParser.Compound_assignmentContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(PinescriptParser.Function_declarationContext,0)


        def type_declaration(self):
            return self.getTypedRuleContext(PinescriptParser.Type_declarationContext,0)


        def structure_statement(self):
            return self.getTypedRuleContext(PinescriptParser.Structure_statementContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_compound_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_statement" ):
                listener.enterCompound_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_statement" ):
                listener.exitCompound_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_statement" ):
                return visitor.visitCompound_statement(self)
            else:
                return visitor.visitChildren(self)




    def compound_statement(self):

        localctx = PinescriptParser.Compound_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compound_statement)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.compound_assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.function_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.type_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 250
                self.structure_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Simple_statementContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Simple_statementContext,i)


        def NEWLINE(self):
            return self.getToken(PinescriptParser.NEWLINE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.COMMA)
            else:
                return self.getToken(PinescriptParser.COMMA, i)

        def getRuleIndex(self):
            return PinescriptParser.RULE_simple_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_statements" ):
                listener.enterSimple_statements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_statements" ):
                listener.exitSimple_statements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_statements" ):
                return visitor.visitSimple_statements(self)
            else:
                return visitor.visitChildren(self)




    def simple_statements(self):

        localctx = PinescriptParser.Simple_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_simple_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.simple_statement()
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 254
                    self.match(PinescriptParser.COMMA)
                    self.state = 255
                    self.simple_statement() 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 261
                self.match(PinescriptParser.COMMA)


            self.state = 264
            self.match(PinescriptParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_assignment(self):
            return self.getTypedRuleContext(PinescriptParser.Simple_assignmentContext,0)


        def expression_statement(self):
            return self.getTypedRuleContext(PinescriptParser.Expression_statementContext,0)


        def import_statement(self):
            return self.getTypedRuleContext(PinescriptParser.Import_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(PinescriptParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(PinescriptParser.Continue_statementContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_simple_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_statement" ):
                listener.enterSimple_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_statement" ):
                listener.exitSimple_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_statement" ):
                return visitor.visitSimple_statement(self)
            else:
                return visitor.visitChildren(self)




    def simple_statement(self):

        localctx = PinescriptParser.Simple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_simple_statement)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.simple_assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.expression_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.import_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 269
                self.break_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 270
                self.continue_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compound_variable_initialization(self):
            return self.getTypedRuleContext(PinescriptParser.Compound_variable_initializationContext,0)


        def compound_reassignment(self):
            return self.getTypedRuleContext(PinescriptParser.Compound_reassignmentContext,0)


        def compound_augassignment(self):
            return self.getTypedRuleContext(PinescriptParser.Compound_augassignmentContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_compound_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_assignment" ):
                listener.enterCompound_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_assignment" ):
                listener.exitCompound_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_assignment" ):
                return visitor.visitCompound_assignment(self)
            else:
                return visitor.visitChildren(self)




    def compound_assignment(self):

        localctx = PinescriptParser.Compound_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_compound_assignment)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.compound_variable_initialization()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.compound_reassignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.compound_augassignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_variable_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compound_name_initialization(self):
            return self.getTypedRuleContext(PinescriptParser.Compound_name_initializationContext,0)


        def compound_tuple_initialization(self):
            return self.getTypedRuleContext(PinescriptParser.Compound_tuple_initializationContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_compound_variable_initialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_variable_initialization" ):
                listener.enterCompound_variable_initialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_variable_initialization" ):
                listener.exitCompound_variable_initialization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_variable_initialization" ):
                return visitor.visitCompound_variable_initialization(self)
            else:
                return visitor.visitChildren(self)




    def compound_variable_initialization(self):

        localctx = PinescriptParser.Compound_variable_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_compound_variable_initialization)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 16, 17, 20, 21, 24, 26, 27, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.compound_name_initialization()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.compound_tuple_initialization()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_name_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(PinescriptParser.Variable_declarationContext,0)


        def EQUAL(self):
            return self.getToken(PinescriptParser.EQUAL, 0)

        def structure_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Structure_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_compound_name_initialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_name_initialization" ):
                listener.enterCompound_name_initialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_name_initialization" ):
                listener.exitCompound_name_initialization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_name_initialization" ):
                return visitor.visitCompound_name_initialization(self)
            else:
                return visitor.visitChildren(self)




    def compound_name_initialization(self):

        localctx = PinescriptParser.Compound_name_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_compound_name_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.variable_declaration()
            self.state = 283
            self.match(PinescriptParser.EQUAL)
            self.state = 284
            self.structure_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_tuple_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple_declaration(self):
            return self.getTypedRuleContext(PinescriptParser.Tuple_declarationContext,0)


        def EQUAL(self):
            return self.getToken(PinescriptParser.EQUAL, 0)

        def structure_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Structure_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_compound_tuple_initialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_tuple_initialization" ):
                listener.enterCompound_tuple_initialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_tuple_initialization" ):
                listener.exitCompound_tuple_initialization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_tuple_initialization" ):
                return visitor.visitCompound_tuple_initialization(self)
            else:
                return visitor.visitChildren(self)




    def compound_tuple_initialization(self):

        localctx = PinescriptParser.Compound_tuple_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_compound_tuple_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.tuple_declaration()
            self.state = 287
            self.match(PinescriptParser.EQUAL)
            self.state = 288
            self.structure_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_reassignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_target(self):
            return self.getTypedRuleContext(PinescriptParser.Assignment_targetContext,0)


        def COLONEQUAL(self):
            return self.getToken(PinescriptParser.COLONEQUAL, 0)

        def structure_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Structure_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_compound_reassignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_reassignment" ):
                listener.enterCompound_reassignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_reassignment" ):
                listener.exitCompound_reassignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_reassignment" ):
                return visitor.visitCompound_reassignment(self)
            else:
                return visitor.visitChildren(self)




    def compound_reassignment(self):

        localctx = PinescriptParser.Compound_reassignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_compound_reassignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.assignment_target()
            self.state = 291
            self.match(PinescriptParser.COLONEQUAL)
            self.state = 292
            self.structure_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_augassignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_target(self):
            return self.getTypedRuleContext(PinescriptParser.Assignment_targetContext,0)


        def augassign_op(self):
            return self.getTypedRuleContext(PinescriptParser.Augassign_opContext,0)


        def structure_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Structure_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_compound_augassignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_augassignment" ):
                listener.enterCompound_augassignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_augassignment" ):
                listener.exitCompound_augassignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_augassignment" ):
                return visitor.visitCompound_augassignment(self)
            else:
                return visitor.visitChildren(self)




    def compound_augassignment(self):

        localctx = PinescriptParser.Compound_augassignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_compound_augassignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.assignment_target()
            self.state = 295
            self.augassign_op()
            self.state = 296
            self.structure_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(PinescriptParser.NameContext,0)


        def LPAR(self):
            return self.getToken(PinescriptParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(PinescriptParser.RPAR, 0)

        def RARROW(self):
            return self.getToken(PinescriptParser.RARROW, 0)

        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def EXPORT(self):
            return self.getToken(PinescriptParser.EXPORT, 0)

        def METHOD(self):
            return self.getToken(PinescriptParser.METHOD, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(PinescriptParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = PinescriptParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 298
                self.match(PinescriptParser.EXPORT)


            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 301
                self.match(PinescriptParser.METHOD)


            self.state = 304
            self.name()
            self.state = 305
            self.match(PinescriptParser.LPAR)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594058047616) != 0):
                self.state = 306
                self.parameter_list()


            self.state = 309
            self.match(PinescriptParser.RPAR)
            self.state = 310
            self.match(PinescriptParser.RARROW)
            self.state = 311
            self.local_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Parameter_definitionContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Parameter_definitionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.COMMA)
            else:
                return self.getToken(PinescriptParser.COMMA, i)

        def getRuleIndex(self):
            return PinescriptParser.RULE_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_list" ):
                listener.enterParameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_list" ):
                listener.exitParameter_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = PinescriptParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.parameter_definition()
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 314
                    self.match(PinescriptParser.COMMA)
                    self.state = 315
                    self.parameter_definition() 
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 321
                self.match(PinescriptParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_store(self):
            return self.getTypedRuleContext(PinescriptParser.Name_storeContext,0)


        def type_specification(self):
            return self.getTypedRuleContext(PinescriptParser.Type_specificationContext,0)


        def EQUAL(self):
            return self.getToken(PinescriptParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_parameter_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_definition" ):
                listener.enterParameter_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_definition" ):
                listener.exitParameter_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_definition" ):
                return visitor.visitParameter_definition(self)
            else:
                return visitor.visitChildren(self)




    def parameter_definition(self):

        localctx = PinescriptParser.Parameter_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 324
                self.type_specification()


            self.state = 327
            self.name_store()
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 328
                self.match(PinescriptParser.EQUAL)
                self.state = 329
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(PinescriptParser.TYPE, 0)

        def name(self):
            return self.getTypedRuleContext(PinescriptParser.NameContext,0)


        def NEWLINE(self):
            return self.getToken(PinescriptParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(PinescriptParser.INDENT, 0)

        def field_definitions(self):
            return self.getTypedRuleContext(PinescriptParser.Field_definitionsContext,0)


        def DEDENT(self):
            return self.getToken(PinescriptParser.DEDENT, 0)

        def EXPORT(self):
            return self.getToken(PinescriptParser.EXPORT, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_type_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_declaration" ):
                listener.enterType_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_declaration" ):
                listener.exitType_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_declaration" ):
                return visitor.visitType_declaration(self)
            else:
                return visitor.visitChildren(self)




    def type_declaration(self):

        localctx = PinescriptParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_type_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 332
                self.match(PinescriptParser.EXPORT)


            self.state = 335
            self.match(PinescriptParser.TYPE)
            self.state = 336
            self.name()
            self.state = 337
            self.match(PinescriptParser.NEWLINE)
            self.state = 338
            self.match(PinescriptParser.INDENT)
            self.state = 339
            self.field_definitions()
            self.state = 340
            self.match(PinescriptParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_definitionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Field_definitionContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Field_definitionContext,i)


        def getRuleIndex(self):
            return PinescriptParser.RULE_field_definitions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_definitions" ):
                listener.enterField_definitions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_definitions" ):
                listener.exitField_definitions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_definitions" ):
                return visitor.visitField_definitions(self)
            else:
                return visitor.visitChildren(self)




    def field_definitions(self):

        localctx = PinescriptParser.Field_definitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_field_definitions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 342
                self.field_definition()
                self.state = 345 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594058047616) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specification(self):
            return self.getTypedRuleContext(PinescriptParser.Type_specificationContext,0)


        def name_store(self):
            return self.getTypedRuleContext(PinescriptParser.Name_storeContext,0)


        def NEWLINE(self):
            return self.getToken(PinescriptParser.NEWLINE, 0)

        def EQUAL(self):
            return self.getToken(PinescriptParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_field_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_definition" ):
                listener.enterField_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_definition" ):
                listener.exitField_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_definition" ):
                return visitor.visitField_definition(self)
            else:
                return visitor.visitChildren(self)




    def field_definition(self):

        localctx = PinescriptParser.Field_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_field_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.type_specification()
            self.state = 348
            self.name_store()
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 349
                self.match(PinescriptParser.EQUAL)
                self.state = 350
                self.expression()


            self.state = 353
            self.match(PinescriptParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_structure(self):
            return self.getTypedRuleContext(PinescriptParser.If_structureContext,0)


        def for_structure(self):
            return self.getTypedRuleContext(PinescriptParser.For_structureContext,0)


        def while_structure(self):
            return self.getTypedRuleContext(PinescriptParser.While_structureContext,0)


        def switch_structure(self):
            return self.getTypedRuleContext(PinescriptParser.Switch_structureContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructure" ):
                listener.enterStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructure" ):
                listener.exitStructure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructure" ):
                return visitor.visitStructure(self)
            else:
                return visitor.visitChildren(self)




    def structure(self):

        localctx = PinescriptParser.StructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_structure)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.if_structure()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.for_structure()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 357
                self.while_structure()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 358
                self.switch_structure()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structure_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structure(self):
            return self.getTypedRuleContext(PinescriptParser.StructureContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_structure_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructure_statement" ):
                listener.enterStructure_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructure_statement" ):
                listener.exitStructure_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructure_statement" ):
                return visitor.visitStructure_statement(self)
            else:
                return visitor.visitChildren(self)




    def structure_statement(self):

        localctx = PinescriptParser.Structure_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_structure_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.structure()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structure_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structure(self):
            return self.getTypedRuleContext(PinescriptParser.StructureContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_structure_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructure_expression" ):
                listener.enterStructure_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructure_expression" ):
                listener.exitStructure_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructure_expression" ):
                return visitor.visitStructure_expression(self)
            else:
                return visitor.visitChildren(self)




    def structure_expression(self):

        localctx = PinescriptParser.Structure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_structure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.structure()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_structureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_structure_elif(self):
            return self.getTypedRuleContext(PinescriptParser.If_structure_elifContext,0)


        def if_structure_else(self):
            return self.getTypedRuleContext(PinescriptParser.If_structure_elseContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_if_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_structure" ):
                listener.enterIf_structure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_structure" ):
                listener.exitIf_structure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_structure" ):
                return visitor.visitIf_structure(self)
            else:
                return visitor.visitChildren(self)




    def if_structure(self):

        localctx = PinescriptParser.If_structureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_if_structure)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.if_structure_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.if_structure_else()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_structure_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PinescriptParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def elif_structure(self):
            return self.getTypedRuleContext(PinescriptParser.Elif_structureContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_if_structure_elif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_structure_elif" ):
                listener.enterIf_structure_elif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_structure_elif" ):
                listener.exitIf_structure_elif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_structure_elif" ):
                return visitor.visitIf_structure_elif(self)
            else:
                return visitor.visitChildren(self)




    def if_structure_elif(self):

        localctx = PinescriptParser.If_structure_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_if_structure_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(PinescriptParser.IF)
            self.state = 370
            self.expression()
            self.state = 371
            self.local_block()
            self.state = 372
            self.elif_structure()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_structure_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PinescriptParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def else_block(self):
            return self.getTypedRuleContext(PinescriptParser.Else_blockContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_if_structure_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_structure_else" ):
                listener.enterIf_structure_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_structure_else" ):
                listener.exitIf_structure_else(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_structure_else" ):
                return visitor.visitIf_structure_else(self)
            else:
                return visitor.visitChildren(self)




    def if_structure_else(self):

        localctx = PinescriptParser.If_structure_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_structure_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(PinescriptParser.IF)
            self.state = 375
            self.expression()
            self.state = 376
            self.local_block()
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 377
                self.else_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_structureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_structure_elif(self):
            return self.getTypedRuleContext(PinescriptParser.Elif_structure_elifContext,0)


        def elif_structure_else(self):
            return self.getTypedRuleContext(PinescriptParser.Elif_structure_elseContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_elif_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_structure" ):
                listener.enterElif_structure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_structure" ):
                listener.exitElif_structure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_structure" ):
                return visitor.visitElif_structure(self)
            else:
                return visitor.visitChildren(self)




    def elif_structure(self):

        localctx = PinescriptParser.Elif_structureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elif_structure)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.elif_structure_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.elif_structure_else()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_structure_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(PinescriptParser.ELSE, 0)

        def IF(self):
            return self.getToken(PinescriptParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def elif_structure(self):
            return self.getTypedRuleContext(PinescriptParser.Elif_structureContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_elif_structure_elif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_structure_elif" ):
                listener.enterElif_structure_elif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_structure_elif" ):
                listener.exitElif_structure_elif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_structure_elif" ):
                return visitor.visitElif_structure_elif(self)
            else:
                return visitor.visitChildren(self)




    def elif_structure_elif(self):

        localctx = PinescriptParser.Elif_structure_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elif_structure_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(PinescriptParser.ELSE)
            self.state = 385
            self.match(PinescriptParser.IF)
            self.state = 386
            self.expression()
            self.state = 387
            self.local_block()
            self.state = 388
            self.elif_structure()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_structure_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(PinescriptParser.ELSE, 0)

        def IF(self):
            return self.getToken(PinescriptParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def else_block(self):
            return self.getTypedRuleContext(PinescriptParser.Else_blockContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_elif_structure_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_structure_else" ):
                listener.enterElif_structure_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_structure_else" ):
                listener.exitElif_structure_else(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_structure_else" ):
                return visitor.visitElif_structure_else(self)
            else:
                return visitor.visitChildren(self)




    def elif_structure_else(self):

        localctx = PinescriptParser.Elif_structure_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elif_structure_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(PinescriptParser.ELSE)
            self.state = 391
            self.match(PinescriptParser.IF)
            self.state = 392
            self.expression()
            self.state = 393
            self.local_block()
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 394
                self.else_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(PinescriptParser.ELSE, 0)

        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_else_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_block" ):
                listener.enterElse_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_block" ):
                listener.exitElse_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_block" ):
                return visitor.visitElse_block(self)
            else:
                return visitor.visitChildren(self)




    def else_block(self):

        localctx = PinescriptParser.Else_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(PinescriptParser.ELSE)
            self.state = 398
            self.local_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_structureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_structure_to(self):
            return self.getTypedRuleContext(PinescriptParser.For_structure_toContext,0)


        def for_structure_in(self):
            return self.getTypedRuleContext(PinescriptParser.For_structure_inContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_for_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_structure" ):
                listener.enterFor_structure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_structure" ):
                listener.exitFor_structure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_structure" ):
                return visitor.visitFor_structure(self)
            else:
                return visitor.visitChildren(self)




    def for_structure(self):

        localctx = PinescriptParser.For_structureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_structure)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.for_structure_to()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.for_structure_in()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_structure_toContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(PinescriptParser.FOR, 0)

        def for_iterator(self):
            return self.getTypedRuleContext(PinescriptParser.For_iteratorContext,0)


        def EQUAL(self):
            return self.getToken(PinescriptParser.EQUAL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.ExpressionContext,i)


        def TO(self):
            return self.getToken(PinescriptParser.TO, 0)

        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def BY(self):
            return self.getToken(PinescriptParser.BY, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_for_structure_to

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_structure_to" ):
                listener.enterFor_structure_to(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_structure_to" ):
                listener.exitFor_structure_to(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_structure_to" ):
                return visitor.visitFor_structure_to(self)
            else:
                return visitor.visitChildren(self)




    def for_structure_to(self):

        localctx = PinescriptParser.For_structure_toContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_structure_to)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(PinescriptParser.FOR)
            self.state = 405
            self.for_iterator()
            self.state = 406
            self.match(PinescriptParser.EQUAL)
            self.state = 407
            self.expression()
            self.state = 408
            self.match(PinescriptParser.TO)
            self.state = 409
            self.expression()
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 410
                self.match(PinescriptParser.BY)
                self.state = 411
                self.expression()


            self.state = 414
            self.local_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_structure_inContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(PinescriptParser.FOR, 0)

        def for_iterator(self):
            return self.getTypedRuleContext(PinescriptParser.For_iteratorContext,0)


        def IN(self):
            return self.getToken(PinescriptParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_for_structure_in

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_structure_in" ):
                listener.enterFor_structure_in(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_structure_in" ):
                listener.exitFor_structure_in(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_structure_in" ):
                return visitor.visitFor_structure_in(self)
            else:
                return visitor.visitChildren(self)




    def for_structure_in(self):

        localctx = PinescriptParser.For_structure_inContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_structure_in)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(PinescriptParser.FOR)
            self.state = 417
            self.for_iterator()
            self.state = 418
            self.match(PinescriptParser.IN)
            self.state = 419
            self.expression()
            self.state = 420
            self.local_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_iteratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_store(self):
            return self.getTypedRuleContext(PinescriptParser.Name_storeContext,0)


        def tuple_declaration(self):
            return self.getTypedRuleContext(PinescriptParser.Tuple_declarationContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_for_iterator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_iterator" ):
                listener.enterFor_iterator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_iterator" ):
                listener.exitFor_iterator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_iterator" ):
                return visitor.visitFor_iterator(self)
            else:
                return visitor.visitChildren(self)




    def for_iterator(self):

        localctx = PinescriptParser.For_iteratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_iterator)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 16, 17, 20, 21, 24, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.name_store()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.tuple_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_structureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(PinescriptParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_while_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_structure" ):
                listener.enterWhile_structure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_structure" ):
                listener.exitWhile_structure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_structure" ):
                return visitor.visitWhile_structure(self)
            else:
                return visitor.visitChildren(self)




    def while_structure(self):

        localctx = PinescriptParser.While_structureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_while_structure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(PinescriptParser.WHILE)
            self.state = 427
            self.expression()
            self.state = 428
            self.local_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_structureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(PinescriptParser.SWITCH, 0)

        def NEWLINE(self):
            return self.getToken(PinescriptParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(PinescriptParser.INDENT, 0)

        def switch_cases(self):
            return self.getTypedRuleContext(PinescriptParser.Switch_casesContext,0)


        def DEDENT(self):
            return self.getToken(PinescriptParser.DEDENT, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_switch_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_structure" ):
                listener.enterSwitch_structure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_structure" ):
                listener.exitSwitch_structure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_structure" ):
                return visitor.visitSwitch_structure(self)
            else:
                return visitor.visitChildren(self)




    def switch_structure(self):

        localctx = PinescriptParser.Switch_structureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_switch_structure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(PinescriptParser.SWITCH)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080969466423478400) != 0):
                self.state = 431
                self.expression()


            self.state = 434
            self.match(PinescriptParser.NEWLINE)
            self.state = 435
            self.match(PinescriptParser.INDENT)
            self.state = 436
            self.switch_cases()
            self.state = 437
            self.match(PinescriptParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_casesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switch_pattern_case(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Switch_pattern_caseContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Switch_pattern_caseContext,i)


        def switch_default_case(self):
            return self.getTypedRuleContext(PinescriptParser.Switch_default_caseContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_switch_cases

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_cases" ):
                listener.enterSwitch_cases(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_cases" ):
                listener.exitSwitch_cases(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_cases" ):
                return visitor.visitSwitch_cases(self)
            else:
                return visitor.visitChildren(self)




    def switch_cases(self):

        localctx = PinescriptParser.Switch_casesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_switch_cases)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 439
                self.switch_pattern_case()
                self.state = 442 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1080969466423478400) != 0)):
                    break

            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 444
                self.switch_default_case()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_pattern_caseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def RARROW(self):
            return self.getToken(PinescriptParser.RARROW, 0)

        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_switch_pattern_case

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_pattern_case" ):
                listener.enterSwitch_pattern_case(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_pattern_case" ):
                listener.exitSwitch_pattern_case(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_pattern_case" ):
                return visitor.visitSwitch_pattern_case(self)
            else:
                return visitor.visitChildren(self)




    def switch_pattern_case(self):

        localctx = PinescriptParser.Switch_pattern_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_switch_pattern_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.expression()
            self.state = 448
            self.match(PinescriptParser.RARROW)
            self.state = 449
            self.local_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_default_caseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RARROW(self):
            return self.getToken(PinescriptParser.RARROW, 0)

        def local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Local_blockContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_switch_default_case

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_default_case" ):
                listener.enterSwitch_default_case(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_default_case" ):
                listener.exitSwitch_default_case(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_default_case" ):
                return visitor.visitSwitch_default_case(self)
            else:
                return visitor.visitChildren(self)




    def switch_default_case(self):

        localctx = PinescriptParser.Switch_default_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_switch_default_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(PinescriptParser.RARROW)
            self.state = 452
            self.local_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indented_local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Indented_local_blockContext,0)


        def inline_local_block(self):
            return self.getTypedRuleContext(PinescriptParser.Inline_local_blockContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_local_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_block" ):
                listener.enterLocal_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_block" ):
                listener.exitLocal_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_block" ):
                return visitor.visitLocal_block(self)
            else:
                return visitor.visitChildren(self)




    def local_block(self):

        localctx = PinescriptParser.Local_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_local_block)
        try:
            self.state = 456
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [60]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.indented_local_block()
                pass
            elif token in [5, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 28, 29, 31, 45, 46, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
                self.inline_local_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indented_local_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(PinescriptParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(PinescriptParser.INDENT, 0)

        def statements(self):
            return self.getTypedRuleContext(PinescriptParser.StatementsContext,0)


        def DEDENT(self):
            return self.getToken(PinescriptParser.DEDENT, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_indented_local_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndented_local_block" ):
                listener.enterIndented_local_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndented_local_block" ):
                listener.exitIndented_local_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndented_local_block" ):
                return visitor.visitIndented_local_block(self)
            else:
                return visitor.visitChildren(self)




    def indented_local_block(self):

        localctx = PinescriptParser.Indented_local_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_indented_local_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(PinescriptParser.NEWLINE)
            self.state = 459
            self.match(PinescriptParser.INDENT)
            self.state = 460
            self.statements()
            self.state = 461
            self.match(PinescriptParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inline_local_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(PinescriptParser.StatementContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_inline_local_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_local_block" ):
                listener.enterInline_local_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_local_block" ):
                listener.exitInline_local_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInline_local_block" ):
                return visitor.visitInline_local_block(self)
            else:
                return visitor.visitChildren(self)




    def inline_local_block(self):

        localctx = PinescriptParser.Inline_local_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_inline_local_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_variable_initialization(self):
            return self.getTypedRuleContext(PinescriptParser.Simple_variable_initializationContext,0)


        def simple_reassignment(self):
            return self.getTypedRuleContext(PinescriptParser.Simple_reassignmentContext,0)


        def simple_augassignment(self):
            return self.getTypedRuleContext(PinescriptParser.Simple_augassignmentContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_simple_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_assignment" ):
                listener.enterSimple_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_assignment" ):
                listener.exitSimple_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_assignment" ):
                return visitor.visitSimple_assignment(self)
            else:
                return visitor.visitChildren(self)




    def simple_assignment(self):

        localctx = PinescriptParser.Simple_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_simple_assignment)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.simple_variable_initialization()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.simple_reassignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.simple_augassignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_variable_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_name_initialization(self):
            return self.getTypedRuleContext(PinescriptParser.Simple_name_initializationContext,0)


        def simple_tuple_initialization(self):
            return self.getTypedRuleContext(PinescriptParser.Simple_tuple_initializationContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_simple_variable_initialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_variable_initialization" ):
                listener.enterSimple_variable_initialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_variable_initialization" ):
                listener.exitSimple_variable_initialization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_variable_initialization" ):
                return visitor.visitSimple_variable_initialization(self)
            else:
                return visitor.visitChildren(self)




    def simple_variable_initialization(self):

        localctx = PinescriptParser.Simple_variable_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_simple_variable_initialization)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 16, 17, 20, 21, 24, 26, 27, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.simple_name_initialization()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.simple_tuple_initialization()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_name_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(PinescriptParser.Variable_declarationContext,0)


        def EQUAL(self):
            return self.getToken(PinescriptParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_simple_name_initialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_name_initialization" ):
                listener.enterSimple_name_initialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_name_initialization" ):
                listener.exitSimple_name_initialization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_name_initialization" ):
                return visitor.visitSimple_name_initialization(self)
            else:
                return visitor.visitChildren(self)




    def simple_name_initialization(self):

        localctx = PinescriptParser.Simple_name_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_simple_name_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.variable_declaration()
            self.state = 475
            self.match(PinescriptParser.EQUAL)
            self.state = 476
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_tuple_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple_declaration(self):
            return self.getTypedRuleContext(PinescriptParser.Tuple_declarationContext,0)


        def EQUAL(self):
            return self.getToken(PinescriptParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_simple_tuple_initialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_tuple_initialization" ):
                listener.enterSimple_tuple_initialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_tuple_initialization" ):
                listener.exitSimple_tuple_initialization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_tuple_initialization" ):
                return visitor.visitSimple_tuple_initialization(self)
            else:
                return visitor.visitChildren(self)




    def simple_tuple_initialization(self):

        localctx = PinescriptParser.Simple_tuple_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_simple_tuple_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.tuple_declaration()
            self.state = 479
            self.match(PinescriptParser.EQUAL)
            self.state = 480
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_reassignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_target(self):
            return self.getTypedRuleContext(PinescriptParser.Assignment_targetContext,0)


        def COLONEQUAL(self):
            return self.getToken(PinescriptParser.COLONEQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_simple_reassignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_reassignment" ):
                listener.enterSimple_reassignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_reassignment" ):
                listener.exitSimple_reassignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_reassignment" ):
                return visitor.visitSimple_reassignment(self)
            else:
                return visitor.visitChildren(self)




    def simple_reassignment(self):

        localctx = PinescriptParser.Simple_reassignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_simple_reassignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.assignment_target()
            self.state = 483
            self.match(PinescriptParser.COLONEQUAL)
            self.state = 484
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_augassignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_target(self):
            return self.getTypedRuleContext(PinescriptParser.Assignment_targetContext,0)


        def augassign_op(self):
            return self.getTypedRuleContext(PinescriptParser.Augassign_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_simple_augassignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_augassignment" ):
                listener.enterSimple_augassignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_augassignment" ):
                listener.exitSimple_augassignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_augassignment" ):
                return visitor.visitSimple_augassignment(self)
            else:
                return visitor.visitChildren(self)




    def simple_augassignment(self):

        localctx = PinescriptParser.Simple_augassignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_simple_augassignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.assignment_target()
            self.state = 487
            self.augassign_op()
            self.state = 488
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Conditional_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PinescriptParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.conditional_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_expression_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_statement" ):
                listener.enterExpression_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_statement" ):
                listener.exitExpression_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_statement" ):
                return visitor.visitExpression_statement(self)
            else:
                return visitor.visitChildren(self)




    def expression_statement(self):

        localctx = PinescriptParser.Expression_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expression_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional_expression_rule(self):
            return self.getTypedRuleContext(PinescriptParser.Conditional_expression_ruleContext,0)


        def disjunction_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Disjunction_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_conditional_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_expression" ):
                listener.enterConditional_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_expression" ):
                listener.exitConditional_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_expression" ):
                return visitor.visitConditional_expression(self)
            else:
                return visitor.visitChildren(self)




    def conditional_expression(self):

        localctx = PinescriptParser.Conditional_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_conditional_expression)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.conditional_expression_rule()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.disjunction_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_expression_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def disjunction_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Disjunction_expressionContext,0)


        def QUESTION(self):
            return self.getToken(PinescriptParser.QUESTION, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.ExpressionContext,i)


        def COLON(self):
            return self.getToken(PinescriptParser.COLON, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_conditional_expression_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_expression_rule" ):
                listener.enterConditional_expression_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_expression_rule" ):
                listener.exitConditional_expression_rule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_expression_rule" ):
                return visitor.visitConditional_expression_rule(self)
            else:
                return visitor.visitChildren(self)




    def conditional_expression_rule(self):

        localctx = PinescriptParser.Conditional_expression_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_conditional_expression_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.disjunction_expression()
            self.state = 499
            self.match(PinescriptParser.QUESTION)
            self.state = 500
            self.expression()
            self.state = 501
            self.match(PinescriptParser.COLON)
            self.state = 502
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Disjunction_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def disjunction_expression_rule(self):
            return self.getTypedRuleContext(PinescriptParser.Disjunction_expression_ruleContext,0)


        def conjunction_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Conjunction_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_disjunction_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction_expression" ):
                listener.enterDisjunction_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction_expression" ):
                listener.exitDisjunction_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunction_expression" ):
                return visitor.visitDisjunction_expression(self)
            else:
                return visitor.visitChildren(self)




    def disjunction_expression(self):

        localctx = PinescriptParser.Disjunction_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_disjunction_expression)
        try:
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.disjunction_expression_rule()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                self.conjunction_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Disjunction_expression_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjunction_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Conjunction_expressionContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Conjunction_expressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.OR)
            else:
                return self.getToken(PinescriptParser.OR, i)

        def getRuleIndex(self):
            return PinescriptParser.RULE_disjunction_expression_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction_expression_rule" ):
                listener.enterDisjunction_expression_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction_expression_rule" ):
                listener.exitDisjunction_expression_rule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunction_expression_rule" ):
                return visitor.visitDisjunction_expression_rule(self)
            else:
                return visitor.visitChildren(self)




    def disjunction_expression_rule(self):

        localctx = PinescriptParser.Disjunction_expression_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_disjunction_expression_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.conjunction_expression()
            self.state = 511 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 509
                self.match(PinescriptParser.OR)
                self.state = 510
                self.conjunction_expression()
                self.state = 513 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==19):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conjunction_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjunction_expression_rule(self):
            return self.getTypedRuleContext(PinescriptParser.Conjunction_expression_ruleContext,0)


        def equality_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Equality_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_conjunction_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction_expression" ):
                listener.enterConjunction_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction_expression" ):
                listener.exitConjunction_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction_expression" ):
                return visitor.visitConjunction_expression(self)
            else:
                return visitor.visitChildren(self)




    def conjunction_expression(self):

        localctx = PinescriptParser.Conjunction_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_conjunction_expression)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.conjunction_expression_rule()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 516
                self.equality_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conjunction_expression_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Equality_expressionContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Equality_expressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.AND)
            else:
                return self.getToken(PinescriptParser.AND, i)

        def getRuleIndex(self):
            return PinescriptParser.RULE_conjunction_expression_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction_expression_rule" ):
                listener.enterConjunction_expression_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction_expression_rule" ):
                listener.exitConjunction_expression_rule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction_expression_rule" ):
                return visitor.visitConjunction_expression_rule(self)
            else:
                return visitor.visitChildren(self)




    def conjunction_expression_rule(self):

        localctx = PinescriptParser.Conjunction_expression_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_conjunction_expression_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.equality_expression()
            self.state = 522 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 520
                self.match(PinescriptParser.AND)
                self.state = 521
                self.equality_expression()
                self.state = 524 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equality_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expression_rule(self):
            return self.getTypedRuleContext(PinescriptParser.Equality_expression_ruleContext,0)


        def inequality_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Inequality_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_equality_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality_expression" ):
                listener.enterEquality_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality_expression" ):
                listener.exitEquality_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality_expression" ):
                return visitor.visitEquality_expression(self)
            else:
                return visitor.visitChildren(self)




    def equality_expression(self):

        localctx = PinescriptParser.Equality_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_equality_expression)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.equality_expression_rule()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.inequality_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equality_expression_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inequality_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Inequality_expressionContext,0)


        def equality_trailing_pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Equality_trailing_pairContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Equality_trailing_pairContext,i)


        def getRuleIndex(self):
            return PinescriptParser.RULE_equality_expression_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality_expression_rule" ):
                listener.enterEquality_expression_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality_expression_rule" ):
                listener.exitEquality_expression_rule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality_expression_rule" ):
                return visitor.visitEquality_expression_rule(self)
            else:
                return visitor.visitChildren(self)




    def equality_expression_rule(self):

        localctx = PinescriptParser.Equality_expression_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_equality_expression_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.inequality_expression()
            self.state = 532 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 531
                self.equality_trailing_pair()
                self.state = 534 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36 or _la==37):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equality_trailing_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equal_trailing_pair(self):
            return self.getTypedRuleContext(PinescriptParser.Equal_trailing_pairContext,0)


        def not_equal_trailing_pair(self):
            return self.getTypedRuleContext(PinescriptParser.Not_equal_trailing_pairContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_equality_trailing_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality_trailing_pair" ):
                listener.enterEquality_trailing_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality_trailing_pair" ):
                listener.exitEquality_trailing_pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality_trailing_pair" ):
                return visitor.visitEquality_trailing_pair(self)
            else:
                return visitor.visitChildren(self)




    def equality_trailing_pair(self):

        localctx = PinescriptParser.Equality_trailing_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_equality_trailing_pair)
        try:
            self.state = 538
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 536
                self.equal_trailing_pair()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 537
                self.not_equal_trailing_pair()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equal_trailing_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQEQUAL(self):
            return self.getToken(PinescriptParser.EQEQUAL, 0)

        def inequality_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Inequality_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_equal_trailing_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual_trailing_pair" ):
                listener.enterEqual_trailing_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual_trailing_pair" ):
                listener.exitEqual_trailing_pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual_trailing_pair" ):
                return visitor.visitEqual_trailing_pair(self)
            else:
                return visitor.visitChildren(self)




    def equal_trailing_pair(self):

        localctx = PinescriptParser.Equal_trailing_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_equal_trailing_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(PinescriptParser.EQEQUAL)
            self.state = 541
            self.inequality_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_equal_trailing_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTEQUAL(self):
            return self.getToken(PinescriptParser.NOTEQUAL, 0)

        def inequality_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Inequality_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_not_equal_trailing_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_equal_trailing_pair" ):
                listener.enterNot_equal_trailing_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_equal_trailing_pair" ):
                listener.exitNot_equal_trailing_pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_equal_trailing_pair" ):
                return visitor.visitNot_equal_trailing_pair(self)
            else:
                return visitor.visitChildren(self)




    def not_equal_trailing_pair(self):

        localctx = PinescriptParser.Not_equal_trailing_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_not_equal_trailing_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(PinescriptParser.NOTEQUAL)
            self.state = 544
            self.inequality_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inequality_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inequality_expression_rule(self):
            return self.getTypedRuleContext(PinescriptParser.Inequality_expression_ruleContext,0)


        def additive_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Additive_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_inequality_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInequality_expression" ):
                listener.enterInequality_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInequality_expression" ):
                listener.exitInequality_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInequality_expression" ):
                return visitor.visitInequality_expression(self)
            else:
                return visitor.visitChildren(self)




    def inequality_expression(self):

        localctx = PinescriptParser.Inequality_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_inequality_expression)
        try:
            self.state = 548
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.inequality_expression_rule()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 547
                self.additive_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inequality_expression_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Additive_expressionContext,0)


        def inequality_trailing_pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Inequality_trailing_pairContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Inequality_trailing_pairContext,i)


        def getRuleIndex(self):
            return PinescriptParser.RULE_inequality_expression_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInequality_expression_rule" ):
                listener.enterInequality_expression_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInequality_expression_rule" ):
                listener.exitInequality_expression_rule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInequality_expression_rule" ):
                return visitor.visitInequality_expression_rule(self)
            else:
                return visitor.visitChildren(self)




    def inequality_expression_rule(self):

        localctx = PinescriptParser.Inequality_expression_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_inequality_expression_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.additive_expression(0)
            self.state = 552 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 551
                self.inequality_trailing_pair()
                self.state = 554 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 850403524608) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inequality_trailing_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def less_than_equal_trailing_pair(self):
            return self.getTypedRuleContext(PinescriptParser.Less_than_equal_trailing_pairContext,0)


        def less_than_trailing_pair(self):
            return self.getTypedRuleContext(PinescriptParser.Less_than_trailing_pairContext,0)


        def greater_than_equal_trailing_pair(self):
            return self.getTypedRuleContext(PinescriptParser.Greater_than_equal_trailing_pairContext,0)


        def greater_than_trailing_pair(self):
            return self.getTypedRuleContext(PinescriptParser.Greater_than_trailing_pairContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_inequality_trailing_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInequality_trailing_pair" ):
                listener.enterInequality_trailing_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInequality_trailing_pair" ):
                listener.exitInequality_trailing_pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInequality_trailing_pair" ):
                return visitor.visitInequality_trailing_pair(self)
            else:
                return visitor.visitChildren(self)




    def inequality_trailing_pair(self):

        localctx = PinescriptParser.Inequality_trailing_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_inequality_trailing_pair)
        try:
            self.state = 560
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.less_than_equal_trailing_pair()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
                self.less_than_trailing_pair()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 558
                self.greater_than_equal_trailing_pair()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 4)
                self.state = 559
                self.greater_than_trailing_pair()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Less_than_equal_trailing_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESSEQUAL(self):
            return self.getToken(PinescriptParser.LESSEQUAL, 0)

        def additive_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Additive_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_less_than_equal_trailing_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess_than_equal_trailing_pair" ):
                listener.enterLess_than_equal_trailing_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess_than_equal_trailing_pair" ):
                listener.exitLess_than_equal_trailing_pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess_than_equal_trailing_pair" ):
                return visitor.visitLess_than_equal_trailing_pair(self)
            else:
                return visitor.visitChildren(self)




    def less_than_equal_trailing_pair(self):

        localctx = PinescriptParser.Less_than_equal_trailing_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_less_than_equal_trailing_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(PinescriptParser.LESSEQUAL)
            self.state = 563
            self.additive_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Less_than_trailing_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS(self):
            return self.getToken(PinescriptParser.LESS, 0)

        def additive_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Additive_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_less_than_trailing_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess_than_trailing_pair" ):
                listener.enterLess_than_trailing_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess_than_trailing_pair" ):
                listener.exitLess_than_trailing_pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess_than_trailing_pair" ):
                return visitor.visitLess_than_trailing_pair(self)
            else:
                return visitor.visitChildren(self)




    def less_than_trailing_pair(self):

        localctx = PinescriptParser.Less_than_trailing_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_less_than_trailing_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.match(PinescriptParser.LESS)
            self.state = 566
            self.additive_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Greater_than_equal_trailing_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREATEREQUAL(self):
            return self.getToken(PinescriptParser.GREATEREQUAL, 0)

        def additive_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Additive_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_greater_than_equal_trailing_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreater_than_equal_trailing_pair" ):
                listener.enterGreater_than_equal_trailing_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreater_than_equal_trailing_pair" ):
                listener.exitGreater_than_equal_trailing_pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreater_than_equal_trailing_pair" ):
                return visitor.visitGreater_than_equal_trailing_pair(self)
            else:
                return visitor.visitChildren(self)




    def greater_than_equal_trailing_pair(self):

        localctx = PinescriptParser.Greater_than_equal_trailing_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_greater_than_equal_trailing_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(PinescriptParser.GREATEREQUAL)
            self.state = 569
            self.additive_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Greater_than_trailing_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREATER(self):
            return self.getToken(PinescriptParser.GREATER, 0)

        def additive_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Additive_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_greater_than_trailing_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreater_than_trailing_pair" ):
                listener.enterGreater_than_trailing_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreater_than_trailing_pair" ):
                listener.exitGreater_than_trailing_pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreater_than_trailing_pair" ):
                return visitor.visitGreater_than_trailing_pair(self)
            else:
                return visitor.visitChildren(self)




    def greater_than_trailing_pair(self):

        localctx = PinescriptParser.Greater_than_trailing_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_greater_than_trailing_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(PinescriptParser.GREATER)
            self.state = 572
            self.additive_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additive_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Multiplicative_expressionContext,0)


        def additive_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Additive_expressionContext,0)


        def additive_op(self):
            return self.getTypedRuleContext(PinescriptParser.Additive_opContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_additive_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive_expression" ):
                listener.enterAdditive_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive_expression" ):
                listener.exitAdditive_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_expression" ):
                return visitor.visitAdditive_expression(self)
            else:
                return visitor.visitChildren(self)



    def additive_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PinescriptParser.Additive_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_additive_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.multiplicative_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 583
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PinescriptParser.Additive_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expression)
                    self.state = 577
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 578
                    self.additive_op()
                    self.state = 579
                    self.multiplicative_expression(0) 
                self.state = 585
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Additive_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(PinescriptParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PinescriptParser.MINUS, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_additive_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive_op" ):
                listener.enterAdditive_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive_op" ):
                listener.exitAdditive_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_op" ):
                return visitor.visitAdditive_op(self)
            else:
                return visitor.visitChildren(self)




    def additive_op(self):

        localctx = PinescriptParser.Additive_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_additive_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            _la = self._input.LA(1)
            if not(_la==45 or _la==46):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplicative_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Unary_expressionContext,0)


        def multiplicative_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Multiplicative_expressionContext,0)


        def multiplicative_op(self):
            return self.getTypedRuleContext(PinescriptParser.Multiplicative_opContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_multiplicative_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative_expression" ):
                listener.enterMultiplicative_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative_expression" ):
                listener.exitMultiplicative_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_expression" ):
                return visitor.visitMultiplicative_expression(self)
            else:
                return visitor.visitChildren(self)



    def multiplicative_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PinescriptParser.Multiplicative_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 142
        self.enterRecursionRule(localctx, 142, self.RULE_multiplicative_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.unary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 597
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PinescriptParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                    self.state = 591
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 592
                    self.multiplicative_op()
                    self.state = 593
                    self.unary_expression() 
                self.state = 599
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplicative_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(PinescriptParser.STAR, 0)

        def SLASH(self):
            return self.getToken(PinescriptParser.SLASH, 0)

        def PERCENT(self):
            return self.getToken(PinescriptParser.PERCENT, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_multiplicative_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative_op" ):
                listener.enterMultiplicative_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative_op" ):
                listener.exitMultiplicative_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_op" ):
                return visitor.visitMultiplicative_op(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative_op(self):

        localctx = PinescriptParser.Multiplicative_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_multiplicative_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_op(self):
            return self.getTypedRuleContext(PinescriptParser.Unary_opContext,0)


        def unary_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Unary_expressionContext,0)


        def primary_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Primary_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_unary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expression" ):
                listener.enterUnary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expression" ):
                listener.exitUnary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expression" ):
                return visitor.visitUnary_expression(self)
            else:
                return visitor.visitChildren(self)




    def unary_expression(self):

        localctx = PinescriptParser.Unary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_unary_expression)
        try:
            self.state = 606
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 602
                self.unary_op()
                self.state = 603
                self.unary_expression()
                pass
            elif token in [7, 11, 16, 17, 20, 21, 24, 25, 29, 31, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 605
                self.primary_expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(PinescriptParser.NOT, 0)

        def PLUS(self):
            return self.getToken(PinescriptParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PinescriptParser.MINUS, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_unary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_op" ):
                listener.enterUnary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_op" ):
                listener.exitUnary_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_op" ):
                return visitor.visitUnary_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_op(self):

        localctx = PinescriptParser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 105553116528640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PinescriptParser.RULE_primary_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Primary_expression_attributeContext(Primary_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PinescriptParser.Primary_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Primary_expressionContext,0)

        def DOT(self):
            return self.getToken(PinescriptParser.DOT, 0)
        def name_load(self):
            return self.getTypedRuleContext(PinescriptParser.Name_loadContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression_attribute" ):
                listener.enterPrimary_expression_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression_attribute" ):
                listener.exitPrimary_expression_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression_attribute" ):
                return visitor.visitPrimary_expression_attribute(self)
            else:
                return visitor.visitChildren(self)


    class Primary_expression_callContext(Primary_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PinescriptParser.Primary_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Primary_expressionContext,0)

        def LPAR(self):
            return self.getToken(PinescriptParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(PinescriptParser.RPAR, 0)
        def template_spec_suffix(self):
            return self.getTypedRuleContext(PinescriptParser.Template_spec_suffixContext,0)

        def argument_list(self):
            return self.getTypedRuleContext(PinescriptParser.Argument_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression_call" ):
                listener.enterPrimary_expression_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression_call" ):
                listener.exitPrimary_expression_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression_call" ):
                return visitor.visitPrimary_expression_call(self)
            else:
                return visitor.visitChildren(self)


    class Primary_expression_fallbackContext(Primary_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PinescriptParser.Primary_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Atomic_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression_fallback" ):
                listener.enterPrimary_expression_fallback(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression_fallback" ):
                listener.exitPrimary_expression_fallback(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression_fallback" ):
                return visitor.visitPrimary_expression_fallback(self)
            else:
                return visitor.visitChildren(self)


    class Primary_expression_subscriptContext(Primary_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PinescriptParser.Primary_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Primary_expressionContext,0)

        def LSQB(self):
            return self.getToken(PinescriptParser.LSQB, 0)
        def subscript_slice(self):
            return self.getTypedRuleContext(PinescriptParser.Subscript_sliceContext,0)

        def RSQB(self):
            return self.getToken(PinescriptParser.RSQB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression_subscript" ):
                listener.enterPrimary_expression_subscript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression_subscript" ):
                listener.exitPrimary_expression_subscript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression_subscript" ):
                return visitor.visitPrimary_expression_subscript(self)
            else:
                return visitor.visitChildren(self)



    def primary_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PinescriptParser.Primary_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 150
        self.enterRecursionRule(localctx, 150, self.RULE_primary_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PinescriptParser.Primary_expression_fallbackContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 611
            self.atomic_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 632
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 630
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = PinescriptParser.Primary_expression_attributeContext(self, PinescriptParser.Primary_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expression)
                        self.state = 613
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 614
                        self.match(PinescriptParser.DOT)
                        self.state = 615
                        self.name_load()
                        pass

                    elif la_ == 2:
                        localctx = PinescriptParser.Primary_expression_callContext(self, PinescriptParser.Primary_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expression)
                        self.state = 616
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 618
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==33:
                            self.state = 617
                            self.template_spec_suffix()


                        self.state = 620
                        self.match(PinescriptParser.LPAR)
                        self.state = 622
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080969466423478400) != 0):
                            self.state = 621
                            self.argument_list()


                        self.state = 624
                        self.match(PinescriptParser.RPAR)
                        pass

                    elif la_ == 3:
                        localctx = PinescriptParser.Primary_expression_subscriptContext(self, PinescriptParser.Primary_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expression)
                        self.state = 625
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 626
                        self.match(PinescriptParser.LSQB)
                        self.state = 627
                        self.subscript_slice()
                        self.state = 628
                        self.match(PinescriptParser.RSQB)
                        pass

             
                self.state = 634
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Argument_definitionContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Argument_definitionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.COMMA)
            else:
                return self.getToken(PinescriptParser.COMMA, i)

        def getRuleIndex(self):
            return PinescriptParser.RULE_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_list" ):
                listener.enterArgument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_list" ):
                listener.exitArgument_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = PinescriptParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.argument_definition()
            self.state = 640
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 636
                    self.match(PinescriptParser.COMMA)
                    self.state = 637
                    self.argument_definition() 
                self.state = 642
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

            self.state = 644
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 643
                self.match(PinescriptParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def name_store(self):
            return self.getTypedRuleContext(PinescriptParser.Name_storeContext,0)


        def EQUAL(self):
            return self.getToken(PinescriptParser.EQUAL, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_argument_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_definition" ):
                listener.enterArgument_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_definition" ):
                listener.exitArgument_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_definition" ):
                return visitor.visitArgument_definition(self)
            else:
                return visitor.visitChildren(self)




    def argument_definition(self):

        localctx = PinescriptParser.Argument_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_argument_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 646
                self.name_store()
                self.state = 647
                self.match(PinescriptParser.EQUAL)


            self.state = 651
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subscript_sliceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.COMMA)
            else:
                return self.getToken(PinescriptParser.COMMA, i)

        def getRuleIndex(self):
            return PinescriptParser.RULE_subscript_slice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript_slice" ):
                listener.enterSubscript_slice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript_slice" ):
                listener.exitSubscript_slice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubscript_slice" ):
                return visitor.visitSubscript_slice(self)
            else:
                return visitor.visitChildren(self)




    def subscript_slice(self):

        localctx = PinescriptParser.Subscript_sliceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_subscript_slice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 653
            self.expression()
            self.state = 658
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 654
                    self.match(PinescriptParser.COMMA)
                    self.state = 655
                    self.expression() 
                self.state = 660
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

            self.state = 662
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 661
                self.match(PinescriptParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_load(self):
            return self.getTypedRuleContext(PinescriptParser.Name_loadContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Literal_expressionContext,0)


        def grouped_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Grouped_expressionContext,0)


        def tuple_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Tuple_expressionContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_atomic_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomic_expression" ):
                listener.enterAtomic_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomic_expression" ):
                listener.exitAtomic_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_expression" ):
                return visitor.visitAtomic_expression(self)
            else:
                return visitor.visitChildren(self)




    def atomic_expression(self):

        localctx = PinescriptParser.Atomic_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_atomic_expression)
        try:
            self.state = 668
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 16, 17, 20, 21, 24, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 664
                self.name_load()
                pass
            elif token in [11, 25, 57, 58, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 665
                self.literal_expression()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 666
                self.grouped_expression()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 667
                self.tuple_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_number(self):
            return self.getTypedRuleContext(PinescriptParser.Literal_numberContext,0)


        def literal_string(self):
            return self.getTypedRuleContext(PinescriptParser.Literal_stringContext,0)


        def literal_bool(self):
            return self.getTypedRuleContext(PinescriptParser.Literal_boolContext,0)


        def literal_color(self):
            return self.getTypedRuleContext(PinescriptParser.Literal_colorContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_literal_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_expression" ):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_expression" ):
                listener.exitLiteral_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_expression" ):
                return visitor.visitLiteral_expression(self)
            else:
                return visitor.visitChildren(self)




    def literal_expression(self):

        localctx = PinescriptParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_literal_expression)
        try:
            self.state = 674
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 670
                self.literal_number()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
                self.literal_string()
                pass
            elif token in [11, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 672
                self.literal_bool()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 4)
                self.state = 673
                self.literal_color()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(PinescriptParser.NUMBER, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_literal_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_number" ):
                listener.enterLiteral_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_number" ):
                listener.exitLiteral_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_number" ):
                return visitor.visitLiteral_number(self)
            else:
                return visitor.visitChildren(self)




    def literal_number(self):

        localctx = PinescriptParser.Literal_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_literal_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
            self.match(PinescriptParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(PinescriptParser.STRING, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_literal_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_string" ):
                listener.enterLiteral_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_string" ):
                listener.exitLiteral_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_string" ):
                return visitor.visitLiteral_string(self)
            else:
                return visitor.visitChildren(self)




    def literal_string(self):

        localctx = PinescriptParser.Literal_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_literal_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
            self.match(PinescriptParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(PinescriptParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(PinescriptParser.FALSE, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_literal_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_bool" ):
                listener.enterLiteral_bool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_bool" ):
                listener.exitLiteral_bool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_bool" ):
                return visitor.visitLiteral_bool(self)
            else:
                return visitor.visitChildren(self)




    def literal_bool(self):

        localctx = PinescriptParser.Literal_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_literal_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            _la = self._input.LA(1)
            if not(_la==11 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_colorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLOR(self):
            return self.getToken(PinescriptParser.COLOR, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_literal_color

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_color" ):
                listener.enterLiteral_color(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_color" ):
                listener.exitLiteral_color(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_color" ):
                return visitor.visitLiteral_color(self)
            else:
                return visitor.visitChildren(self)




    def literal_color(self):

        localctx = PinescriptParser.Literal_colorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_literal_color)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            self.match(PinescriptParser.COLOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grouped_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(PinescriptParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(PinescriptParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(PinescriptParser.RPAR, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_grouped_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrouped_expression" ):
                listener.enterGrouped_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrouped_expression" ):
                listener.exitGrouped_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouped_expression" ):
                return visitor.visitGrouped_expression(self)
            else:
                return visitor.visitChildren(self)




    def grouped_expression(self):

        localctx = PinescriptParser.Grouped_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_grouped_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.match(PinescriptParser.LPAR)
            self.state = 685
            self.expression()
            self.state = 686
            self.match(PinescriptParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tuple_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQB(self):
            return self.getToken(PinescriptParser.LSQB, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.ExpressionContext,i)


        def RSQB(self):
            return self.getToken(PinescriptParser.RSQB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.COMMA)
            else:
                return self.getToken(PinescriptParser.COMMA, i)

        def getRuleIndex(self):
            return PinescriptParser.RULE_tuple_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_expression" ):
                listener.enterTuple_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_expression" ):
                listener.exitTuple_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_expression" ):
                return visitor.visitTuple_expression(self)
            else:
                return visitor.visitChildren(self)




    def tuple_expression(self):

        localctx = PinescriptParser.Tuple_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_tuple_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.match(PinescriptParser.LSQB)
            self.state = 689
            self.expression()
            self.state = 694
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 690
                    self.match(PinescriptParser.COMMA)
                    self.state = 691
                    self.expression() 
                self.state = 696
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

            self.state = 698
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 697
                self.match(PinescriptParser.COMMA)


            self.state = 700
            self.match(PinescriptParser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(PinescriptParser.IMPORT, 0)

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.NameContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.NameContext,i)


        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.SLASH)
            else:
                return self.getToken(PinescriptParser.SLASH, i)

        def literal_number(self):
            return self.getTypedRuleContext(PinescriptParser.Literal_numberContext,0)


        def AS(self):
            return self.getToken(PinescriptParser.AS, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_import_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_statement" ):
                listener.enterImport_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_statement" ):
                listener.exitImport_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_statement" ):
                return visitor.visitImport_statement(self)
            else:
                return visitor.visitChildren(self)




    def import_statement(self):

        localctx = PinescriptParser.Import_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_import_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            self.match(PinescriptParser.IMPORT)
            self.state = 703
            self.name()
            self.state = 704
            self.match(PinescriptParser.SLASH)
            self.state = 705
            self.name()
            self.state = 706
            self.match(PinescriptParser.SLASH)
            self.state = 707
            self.literal_number()
            self.state = 710
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 708
                self.match(PinescriptParser.AS)
                self.state = 709
                self.name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(PinescriptParser.BREAK, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_break_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_statement" ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_statement" ):
                listener.exitBreak_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = PinescriptParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.match(PinescriptParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(PinescriptParser.CONTINUE, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_continue_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_statement" ):
                listener.enterContinue_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_statement" ):
                listener.exitContinue_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = PinescriptParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self.match(PinescriptParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_store(self):
            return self.getTypedRuleContext(PinescriptParser.Name_storeContext,0)


        def declaration_mode(self):
            return self.getTypedRuleContext(PinescriptParser.Declaration_modeContext,0)


        def type_specification(self):
            return self.getTypedRuleContext(PinescriptParser.Type_specificationContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = PinescriptParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 716
                self.declaration_mode()


            self.state = 720
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 719
                self.type_specification()


            self.state = 722
            self.name_store()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tuple_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQB(self):
            return self.getToken(PinescriptParser.LSQB, 0)

        def name_store(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Name_storeContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Name_storeContext,i)


        def RSQB(self):
            return self.getToken(PinescriptParser.RSQB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.COMMA)
            else:
                return self.getToken(PinescriptParser.COMMA, i)

        def getRuleIndex(self):
            return PinescriptParser.RULE_tuple_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_declaration" ):
                listener.enterTuple_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_declaration" ):
                listener.exitTuple_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_declaration" ):
                return visitor.visitTuple_declaration(self)
            else:
                return visitor.visitChildren(self)




    def tuple_declaration(self):

        localctx = PinescriptParser.Tuple_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_tuple_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 724
            self.match(PinescriptParser.LSQB)
            self.state = 725
            self.name_store()
            self.state = 730
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 726
                    self.match(PinescriptParser.COMMA)
                    self.state = 727
                    self.name_store() 
                self.state = 732
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

            self.state = 734
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 733
                self.match(PinescriptParser.COMMA)


            self.state = 736
            self.match(PinescriptParser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_modeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIP(self):
            return self.getToken(PinescriptParser.VARIP, 0)

        def VAR(self):
            return self.getToken(PinescriptParser.VAR, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_declaration_mode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_mode" ):
                listener.enterDeclaration_mode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_mode" ):
                listener.exitDeclaration_mode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_mode" ):
                return visitor.visitDeclaration_mode(self)
            else:
                return visitor.visitChildren(self)




    def declaration_mode(self):

        localctx = PinescriptParser.Declaration_modeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_declaration_mode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 738
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_targetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_target_attribute(self):
            return self.getTypedRuleContext(PinescriptParser.Assignment_target_attributeContext,0)


        def assignment_target_subscript(self):
            return self.getTypedRuleContext(PinescriptParser.Assignment_target_subscriptContext,0)


        def assignment_target_name(self):
            return self.getTypedRuleContext(PinescriptParser.Assignment_target_nameContext,0)


        def assignment_target_group(self):
            return self.getTypedRuleContext(PinescriptParser.Assignment_target_groupContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_assignment_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_target" ):
                listener.enterAssignment_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_target" ):
                listener.exitAssignment_target(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_target" ):
                return visitor.visitAssignment_target(self)
            else:
                return visitor.visitChildren(self)




    def assignment_target(self):

        localctx = PinescriptParser.Assignment_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_assignment_target)
        try:
            self.state = 744
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 740
                self.assignment_target_attribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 741
                self.assignment_target_subscript()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 742
                self.assignment_target_name()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 743
                self.assignment_target_group()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_target_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Primary_expressionContext,0)


        def DOT(self):
            return self.getToken(PinescriptParser.DOT, 0)

        def name_store(self):
            return self.getTypedRuleContext(PinescriptParser.Name_storeContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_assignment_target_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_target_attribute" ):
                listener.enterAssignment_target_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_target_attribute" ):
                listener.exitAssignment_target_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_target_attribute" ):
                return visitor.visitAssignment_target_attribute(self)
            else:
                return visitor.visitChildren(self)




    def assignment_target_attribute(self):

        localctx = PinescriptParser.Assignment_target_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_assignment_target_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 746
            self.primary_expression(0)
            self.state = 747
            self.match(PinescriptParser.DOT)
            self.state = 748
            self.name_store()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_target_subscriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self):
            return self.getTypedRuleContext(PinescriptParser.Primary_expressionContext,0)


        def LSQB(self):
            return self.getToken(PinescriptParser.LSQB, 0)

        def subscript_slice(self):
            return self.getTypedRuleContext(PinescriptParser.Subscript_sliceContext,0)


        def RSQB(self):
            return self.getToken(PinescriptParser.RSQB, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_assignment_target_subscript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_target_subscript" ):
                listener.enterAssignment_target_subscript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_target_subscript" ):
                listener.exitAssignment_target_subscript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_target_subscript" ):
                return visitor.visitAssignment_target_subscript(self)
            else:
                return visitor.visitChildren(self)




    def assignment_target_subscript(self):

        localctx = PinescriptParser.Assignment_target_subscriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_assignment_target_subscript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 750
            self.primary_expression(0)
            self.state = 751
            self.match(PinescriptParser.LSQB)
            self.state = 752
            self.subscript_slice()
            self.state = 753
            self.match(PinescriptParser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_target_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_store(self):
            return self.getTypedRuleContext(PinescriptParser.Name_storeContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_assignment_target_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_target_name" ):
                listener.enterAssignment_target_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_target_name" ):
                listener.exitAssignment_target_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_target_name" ):
                return visitor.visitAssignment_target_name(self)
            else:
                return visitor.visitChildren(self)




    def assignment_target_name(self):

        localctx = PinescriptParser.Assignment_target_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_assignment_target_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self.name_store()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_target_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(PinescriptParser.LPAR, 0)

        def assignment_target(self):
            return self.getTypedRuleContext(PinescriptParser.Assignment_targetContext,0)


        def RPAR(self):
            return self.getToken(PinescriptParser.RPAR, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_assignment_target_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_target_group" ):
                listener.enterAssignment_target_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_target_group" ):
                listener.exitAssignment_target_group(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_target_group" ):
                return visitor.visitAssignment_target_group(self)
            else:
                return visitor.visitChildren(self)




    def assignment_target_group(self):

        localctx = PinescriptParser.Assignment_target_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_assignment_target_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 757
            self.match(PinescriptParser.LPAR)
            self.state = 758
            self.assignment_target()
            self.state = 759
            self.match(PinescriptParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Augassign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAREQUAL(self):
            return self.getToken(PinescriptParser.STAREQUAL, 0)

        def SLASHEQUAL(self):
            return self.getToken(PinescriptParser.SLASHEQUAL, 0)

        def PERCENTEQUAL(self):
            return self.getToken(PinescriptParser.PERCENTEQUAL, 0)

        def PLUSEQUAL(self):
            return self.getToken(PinescriptParser.PLUSEQUAL, 0)

        def MINEQUAL(self):
            return self.getToken(PinescriptParser.MINEQUAL, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_augassign_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAugassign_op" ):
                listener.enterAugassign_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAugassign_op" ):
                listener.exitAugassign_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAugassign_op" ):
                return visitor.visitAugassign_op(self)
            else:
                return visitor.visitChildren(self)




    def augassign_op(self):

        localctx = PinescriptParser.Augassign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_augassign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 761
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34902897112121344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributed_type_name(self):
            return self.getTypedRuleContext(PinescriptParser.Attributed_type_nameContext,0)


        def type_qualifier(self):
            return self.getTypedRuleContext(PinescriptParser.Type_qualifierContext,0)


        def template_spec_suffix(self):
            return self.getTypedRuleContext(PinescriptParser.Template_spec_suffixContext,0)


        def array_type_suffix(self):
            return self.getTypedRuleContext(PinescriptParser.Array_type_suffixContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_type_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_specification" ):
                listener.enterType_specification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_specification" ):
                listener.exitType_specification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_specification" ):
                return visitor.visitType_specification(self)
            else:
                return visitor.visitChildren(self)




    def type_specification(self):

        localctx = PinescriptParser.Type_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_type_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 764
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.state = 763
                self.type_qualifier()


            self.state = 766
            self.attributed_type_name()
            self.state = 768
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 767
                self.template_spec_suffix()


            self.state = 771
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 770
                self.array_type_suffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_qualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(PinescriptParser.CONST, 0)

        def INPUT(self):
            return self.getToken(PinescriptParser.INPUT, 0)

        def SIMPLE(self):
            return self.getToken(PinescriptParser.SIMPLE, 0)

        def SERIES(self):
            return self.getToken(PinescriptParser.SERIES, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_type_qualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_qualifier" ):
                listener.enterType_qualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_qualifier" ):
                listener.exitType_qualifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_qualifier" ):
                return visitor.visitType_qualifier(self)
            else:
                return visitor.visitChildren(self)




    def type_qualifier(self):

        localctx = PinescriptParser.Type_qualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_type_qualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 773
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3211392) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attributed_type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_load(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Name_loadContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Name_loadContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.DOT)
            else:
                return self.getToken(PinescriptParser.DOT, i)

        def getRuleIndex(self):
            return PinescriptParser.RULE_attributed_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributed_type_name" ):
                listener.enterAttributed_type_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributed_type_name" ):
                listener.exitAttributed_type_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributed_type_name" ):
                return visitor.visitAttributed_type_name(self)
            else:
                return visitor.visitChildren(self)




    def attributed_type_name(self):

        localctx = PinescriptParser.Attributed_type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_attributed_type_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
            self.name_load()
            self.state = 780
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 776
                self.match(PinescriptParser.DOT)
                self.state = 777
                self.name_load()
                self.state = 782
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Template_spec_suffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS(self):
            return self.getToken(PinescriptParser.LESS, 0)

        def GREATER(self):
            return self.getToken(PinescriptParser.GREATER, 0)

        def type_argument_list(self):
            return self.getTypedRuleContext(PinescriptParser.Type_argument_listContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_template_spec_suffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate_spec_suffix" ):
                listener.enterTemplate_spec_suffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate_spec_suffix" ):
                listener.exitTemplate_spec_suffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplate_spec_suffix" ):
                return visitor.visitTemplate_spec_suffix(self)
            else:
                return visitor.visitChildren(self)




    def template_spec_suffix(self):

        localctx = PinescriptParser.Template_spec_suffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_template_spec_suffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 783
            self.match(PinescriptParser.LESS)
            self.state = 785
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594058047616) != 0):
                self.state = 784
                self.type_argument_list()


            self.state = 787
            self.match(PinescriptParser.GREATER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_type_suffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQB(self):
            return self.getToken(PinescriptParser.LSQB, 0)

        def RSQB(self):
            return self.getToken(PinescriptParser.RSQB, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_array_type_suffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_type_suffix" ):
                listener.enterArray_type_suffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_type_suffix" ):
                listener.exitArray_type_suffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type_suffix" ):
                return visitor.visitArray_type_suffix(self)
            else:
                return visitor.visitChildren(self)




    def array_type_suffix(self):

        localctx = PinescriptParser.Array_type_suffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_array_type_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 789
            self.match(PinescriptParser.LSQB)
            self.state = 790
            self.match(PinescriptParser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specification(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.Type_specificationContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.Type_specificationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PinescriptParser.COMMA)
            else:
                return self.getToken(PinescriptParser.COMMA, i)

        def getRuleIndex(self):
            return PinescriptParser.RULE_type_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_argument_list" ):
                listener.enterType_argument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_argument_list" ):
                listener.exitType_argument_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_argument_list" ):
                return visitor.visitType_argument_list(self)
            else:
                return visitor.visitChildren(self)




    def type_argument_list(self):

        localctx = PinescriptParser.Type_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_type_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 792
            self.type_specification()
            self.state = 797
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 793
                    self.match(PinescriptParser.COMMA)
                    self.state = 794
                    self.type_specification() 
                self.state = 799
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

            self.state = 801
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 800
                self.match(PinescriptParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PinescriptParser.NAME, 0)

        def TYPE(self):
            return self.getToken(PinescriptParser.TYPE, 0)

        def METHOD(self):
            return self.getToken(PinescriptParser.METHOD, 0)

        def CONST(self):
            return self.getToken(PinescriptParser.CONST, 0)

        def INPUT(self):
            return self.getToken(PinescriptParser.INPUT, 0)

        def SIMPLE(self):
            return self.getToken(PinescriptParser.SIMPLE, 0)

        def SERIES(self):
            return self.getToken(PinescriptParser.SERIES, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = PinescriptParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 803
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594058047616) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_loadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(PinescriptParser.NameContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_name_load

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_load" ):
                listener.enterName_load(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_load" ):
                listener.exitName_load(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_load" ):
                return visitor.visitName_load(self)
            else:
                return visitor.visitChildren(self)




    def name_load(self):

        localctx = PinescriptParser.Name_loadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_name_load)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 805
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_storeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(PinescriptParser.NameContext,0)


        def getRuleIndex(self):
            return PinescriptParser.RULE_name_store

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_store" ):
                listener.enterName_store(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_store" ):
                listener.exitName_store(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_store" ):
                return visitor.visitName_store(self)
            else:
                return visitor.visitChildren(self)




    def name_store(self):

        localctx = PinescriptParser.Name_storeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_name_store)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 807
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PinescriptParser.CommentContext)
            else:
                return self.getTypedRuleContext(PinescriptParser.CommentContext,i)


        def getRuleIndex(self):
            return PinescriptParser.RULE_comments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComments" ):
                listener.enterComments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComments" ):
                listener.exitComments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComments" ):
                return visitor.visitComments(self)
            else:
                return visitor.visitChildren(self)




    def comments(self):

        localctx = PinescriptParser.CommentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_comments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 810 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 809
                self.comment()
                self.state = 812 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==62):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(PinescriptParser.COMMENT, 0)

        def getRuleIndex(self):
            return PinescriptParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = PinescriptParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 814
            self.match(PinescriptParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[69] = self.additive_expression_sempred
        self._predicates[71] = self.multiplicative_expression_sempred
        self._predicates[75] = self.primary_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def additive_expression_sempred(self, localctx:Additive_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def multiplicative_expression_sempred(self, localctx:Multiplicative_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def primary_expression_sempred(self, localctx:Primary_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




