from jarbas_wake_word_plugin_nyumaya.libnyumaya import NyumayaDetector, FeatureExtractor
from datetime import datetime
from jarbas_wake_word_plugin_nyumaya.record import ArecordStream


def label_stream(graph, sensitivity):
    audio_stream = ArecordStream()

    extractor = FeatureExtractor()
    extactor_gain = 1.0

    detector = NyumayaDetector(graph)
    detector.set_sensitivity(sensitivity)

    bufsize = detector.get_input_data_size()

    print("Version: " + detector.version)

    audio_stream.start()
    try:
        while True:
            frame = audio_stream.read(bufsize * 2, bufsize * 2)
            if not frame:
                continue

            features = extractor.signal_to_mel(frame, extactor_gain)

            prediction = detector.run_detection(features)

            if prediction:
                now = datetime.now().strftime("%d.%b %Y %H:%M:%S")
                print("detected " + now)

    except KeyboardInterrupt:
        print("Terminating")
        audio_stream.stop()


if __name__ == '__main__':
    import argparse
    from os.path import dirname, join

    models_folder = join(dirname(dirname(__file__)), "ovos_ww_plugin_nyumaya_legacy",
                         "models")
    default_model = join(models_folder, "hotwords", "alexa_v1.0.0.premium")

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--model', type=str,
        default=default_model,
        help='Model to use for identification.')

    parser.add_argument(
        '--sens', type=float,
        default='0.5',
        help='Sensitivity for detection. A lower value means more sensitivity, for example,'
             '0.1 will lead to less false positives, but will also be harder to trigger.'
             '0.9 will make it easier to trigger, but lead to more false positives')

    FLAGS, unparsed = parser.parse_known_args()

    label_stream(FLAGS.model, FLAGS.sens)
