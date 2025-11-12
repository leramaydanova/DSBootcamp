import analytics, config, logging

if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO, filename="analytics.log", format="%(asctime)s %(message)s", filemode="w")
        try:
            list = analytics.Research(config.FILE_PATH).file_reader(has_header=False)
            calc = analytics.Research.Calculations(list).counts()
            frac = analytics.Research.Calculations(list).fractions(calc[0], calc[1])
            rand = analytics.Research.Analytics(list).predict_random(config.NUM_OF_STEPS)
            last = analytics.Research.Analytics(list).predict_last()
            analytics.Research.Analytics(list).save_file([list, calc, frac, rand], "report", "txt")
            analytics.Research(config.FILE_PATH).send_message()
        except ValueError as e:
            print(e)
            analytics.Research(config.FILE_PATH).send_message(False)
        except Exception as e:
            print(e)
            analytics.Research(config.FILE_PATH).send_message(False)