from func import r

b = 0


def main(i):
    global b
    b = 0
    if i < 5:
        x, b = r(0.075, 0.085, i, b, 5)
    elif i < 7:
        x, b = r(0.109, 0.129, i, b, 7)
    elif i < 8:
        x, b = r(0.095, 0.105, i, b, 8)
    elif i < 13:
        x, b = r(0.069, 0.085, i, b, 13)
    elif i < 16:
        x, b = r(0.09, 0.0115, i, b, 16)
    elif i < 19:
        x, b = r(0.085, 0.1, i, b, 19)
    elif i < 30:
        x, b = r(0.055, 0.1, i, b, 30)
    elif i < 40:
        x, b = r(0.08, 0.125, i, b, 40)
    elif i < 50:
        x, b = r(0.12, 0.15, i, b, 50)
    elif i < 52:
        x, b = r(0.075, 0.1, i, b, 52)
    elif i < 58:
        x, b = r(0.05, 0.07, i, b, 58)
    elif i < 59:
        x, b = r(0.03, 0.04, i, b, 59)
    elif i < 60:
        x, b = r(0, 0.005, i, b, 60)
    elif i < 72:
        x, b = r(-0.02, 0, i, b, 72)
    elif i < 74:
        x, b = r(0, 0.007, i, b, 74)
    elif i < 99:
        x, b = r(-0.033, 0, i, b, 99)
    elif i < 101:
        x, b = r(0, 0.01, i, b, 101)
    elif i < 104:
        x, b = r(-0.01, 0, i, b, 104)
    elif i < 109:
        x, b = r(0, 0.02, i, b, 109)
    elif i < 117:
        x, b = r(-0.01, 0, i, b, 117)
    elif i < 137:
        x, b = r(-0.044, -0.029, i, b, 137)
    elif i < 146:
        x, b = r(-0.026, -0.011, i, b, 146)
    elif i < 156:
        x, b = r(-0.045, -0.029, i, b, 156)
    elif i < 158:
        x, b = r(-0.025, -0.015, i, b, 158)
    elif i < 166:
        x, b = r(-0.01, 0.01, i, b, 166)
    elif i < 167:
        x, b = r(-0.013, -0.012, i, b, 167)
    elif i < 168:
        x, b = r(-0.02, -0.019, i, b, 168)
    elif i < 175:
        x, b = r(-0.031, -0.021, i, b, 175)
    elif i < 178:
        x, b = r(-0.05, -0.034, i, b, 178)
    elif i < 183:
        x, b = r(-0.058, -0.049, i, b, 183)
    elif i < 186:
        x, b = r(-0.06, -0.055, i, b, 186)
    elif i < 194:
        x, b = r(-0.048, -0.038, i, b, 194)
    elif i < 198:
        x, b = r(-0.03, -0.023, i, b, 198)
    elif i < 202:
        x, b = r(-0.036, -0.03, i, b, 202)
    elif i < 204:
        x, b = r(-0.046, -0.039, i, b, 204)
    elif i < 209:
        x, b = r(-0.06, -0.05, i, b, 209)
    elif i < 219:
        x, b = r(-0.05, -0.03, i, b, 219)
    elif i < 231:
        x, b = r(-0.031, -0.021, i, b, 231)
    elif i < 233:
        x, b = r(-0.045, -0.035, i, b, 233)
    elif i < 239:
        x, b = r(-0.062, -0.047, i, b, 239)
    elif i < 245:
        x, b = r(-0.078, -0.07, i, b, 245)
    elif i < 252:
        x, b = r(-0.066, -0.059, i, b, 252)
    elif i < 264:
        x, b = r(-0.053, -0.045, i, b, 264)
    elif i < 277:
        x, b = r(-0.061, -0.05, i, b, 277)
    elif i < 290:
        x, b = r(-0.049, -0.039, i, b, 290)
    elif i < 294:
        x, b = r(-0.062, -0.05, i, b, 294)
    elif i < 301:
        x, b = r(-0.07, -0.063, i, b, 301)
    elif i < 321:
        x, b = r(-0.061, -0.049, i, b, 321)
    elif i < 324:
        x, b = r(-0.075, -0.065, i, b, 324)
    elif i < 327:
        x, b = r(-0.098, -0.085, i, b, 327)
    elif i < 331:
        x, b = r(-0.12, -0.1, i, b, 331)
    elif i < 335:
        x, b = r(-0.13, -0.12, i, b, 335)
    elif i < 337:
        x, b = r(-0.12, -0.11, i, b, 337)
    elif i < 340:
        x, b = r(-0.105, -0.09, i, b, 340)
    elif i < 342:
        x, b = r(-0.075, -0.06, i, b, 342)
    elif i < 344:
        x, b = r(-0.06, -0.045, i, b, 344)
    elif i < 346:
        x, b = r(-0.035, -0.025, i, b, 346)
    elif i < 348:
        x, b = r(-0.01, 0, i, b, 348)
    elif i < 358:
        x, b = r(0, 0.013, i, b, 358)
    elif i < 361:
        x, b = r(-0.0125, 0, i, b, 361)
    elif i < 365:
        x, b = r(-0.03, -0.02, i, b, 365)
    elif i < 367:
        x, b = r(-0.04, -0.03, i, b, 367)
    elif i < 370:
        x, b = r(-0.059, -0.049, i, b, 370)
    elif i < 381:
        x, b = r(-0.067, -0.054, i, b, 381)
    elif i < 383:
        x, b = r(-0.07, -0.065, i, b, 383)
    elif i < 390:
        x, b = r(-0.062, -0.049, i, b, 390)
    elif i < 391:
        x, b = r(-0.04, -0.03, i, b, 391)
    elif i < 396:
        x, b = r(-0.03, -0.02, i, b, 396)
    elif i < 399:
        x, b = r(-0.02, 0, i, b, 399)
    elif i < 405:
        x, b = r(0, 0.025, i, b, 405)
    elif i < 407:
        x, b = r(0.03, 0.04, i, b, 407)
    elif i < 408:
        x, b = r(0.04, 0.05, i, b, 408)
    elif i < 410:
        x, b = r(0.06, 0.07, i, b, 410)
    elif i < 412:
        x, b = r(0.08, 0.09, i, b, 412)
    elif i < 415:
        x, b = r(0.09, 0.1, i, b, 415)
    elif i < 417:
        x, b = r(0.1, 0.11, i, b, 417)
    elif i < 418:
        x, b = r(0.12, 0.123, i, b, 418)
    elif i < 421:
        x, b = r(0.09, 0.1, i, b, 421)
    elif i < 424:
        x, b = r(0.06, 0.08, i, b, 424)
    elif i < 425:
        x, b = r(0.04, 0.05, i, b, 425)
    elif i < 431:
        x, b = r(0.078, 0.1, i, b, 431)
    elif i < 432:
        x, b = r(0.13, 0.145, i, b, 432)
    elif i < 433:
        x, b = r(0.145, 0.165, i, b, 433)
    elif i < 442:
        x, b = r(0.15, 0.2, i, b, 442)
    elif i < 452:
        x, b = r(0.23, 0.265, i, b, 452)
    elif i < 454:
        x, b = r(0.19, 0.2, i, b, 454)
    elif i < 455:
        x, b = r(0.165, 0.175, i, b, 455)
    elif i < 459:
        x, b = r(0.13, 0.1475, i, b, 459)
    elif i < 462:
        x, b = r(0.11, 0.13, i, b, 462)
    elif i < 479:
        x, b = r(0.05, 0.09, i, b, 479)
    elif i < 481:
        x, b = r(0.03, 0.04, i, b, 481)
    elif i < 482:
        x, b = r(0.05, 0.06, i, b, 482)
    elif i < 484:
        x, b = r(0.07, 0.082, i, b, 484)
    elif i < 486:
        x, b = r(0.1, 0.12, i, b, 486)
    elif i < 488:
        x, b = r(0.08, 0.1, i, b, 488)
    elif i < 499:
        x, b = r(0.1, 0.13, i, b, 499)
    else:
        x, b = r(0.13, 0.145, i, b, 500)
    return x
