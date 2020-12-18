## Description
Mycroft wake word plugin for [Nyumaya](https://github.com/nyumaya) version 1.0.0

The "plugins" are pip install-able modules that provide new engines for mycroft

more info in the [docs](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/plugins)

### Performance
- Pi Zero: CPU 40%
- Pi 3: CPU
- Pi 4: CPU one core: 4%

## Install

`mycroft-pip install jarbas-wake-word-plugin-nyumaya-premium`

## Configuration

The default free wake words are included with this plugin

Add the following to your hotwords section in mycroft.conf 

```json
  "hotwords": {
    "alexa": {
        "module": "nyumaya_premium_ww_plug",
        "model": "alexa",
        "sensitivity": 0.5,
        "extractor_gain": 1.0
    },
    "marvin": {
        "module": "nyumaya_premium_ww_plug",
        "model": "marvin",
        "sensitivity": 0.5,
        "extractor_gain": 1.0
    },
    "sheila": {
        "module": "nyumaya_premium_ww_plug",
        "model": "sheila",
        "sensitivity": 0.5,
        "extractor_gain": 1.0
    },
     "firefox": {
        "module": "nyumaya_premium_ww_plug",
        "model": "firefox",
        "sensitivity": 0.5,
        "extractor_gain": 1.0
    }
  }
```

Then select what wakeword to use

```json
 "listener": {
      "wake_word": "alexa"
 }
 
```


# Training your own wake word

You can request new wake words [here](https://nyumaya.com/requesting-custom-keywords/)