import analytics, config

if __name__ == '__main__':
    try:
        list = analytics.Research(config.FILE_PATH).file_reader()
        calc = analytics.Research.Calculations(list).counts()
        frac = analytics.Research.Calculations(list).fractions(calc[0], calc[1])
        rand = analytics.Research.Analytics(list).predict_random(config.NUM_OF_STEPS)
        last = analytics.Research.Analytics(list).predict_last()
        analytics.Research.Analytics(list).save_file([list, calc, frac, rand], "report", "txt")
    except ValueError as e:
        print(e)