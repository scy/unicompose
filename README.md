# unicompose – consistent compose characters, everywhere

I use a lot of different operating systems: macOS, Windows, Linux and even Chrome OS.

Recently, I've watched [Miroslav Šedivý](https://twitter.com/eumiro?lang=de)'s [talk about Compose Keys](https://www.youtube.com/watch?v=g-TlsNUx0RQ) and while I'm not new to the concept, I've decided to give it another try. But, the combinations have to be the same on all of my machines, and of course I don't want to manually keep them in sync.

This project is supposed to generate configs out of a central master config. The documentation is still a bit lacking, but that will improve. It already takes the Chrome OS extension's definition and converts it to a macOS compatible one. More will follow.

## How to set up

First, clone the repo, including submodules:

```sh
git clone --recurse-submodules https://github.com/scy/unicompose.git \
&& cd unicompose
```

Then, follow the OS-specific instructions.

### macOS 10.12 Sierra and higher

My setup is based on [gnarf/osx-compose-key](https://github.com/gnarf/osx-compose-key), which also means that the key to trigger Compose is `§`, or what Karabiner-Elements calls `non_us_backslash`. This basically means that whatever you map to that key will be your Compose key.

If you happen to use an ISO keyboard (with an additional key to the right of the left Shift key), you can get away without using Karabiner-Elements at all; the top-left key on your keyboard (above Tab) is probably your Compose key then.

After setting up any remappings, generate the conversion tree by running this in your terminal:

```sh
mkdir -p ~/Library/KeyBindings \
&& ./convert.py > ~/Library/KeyBindings/DefaultKeyBinding.dict
```

The changes will only apply to an application once you've restarted it; however, you don't need to restart the computer as a whole.

## Acknowledgements

Thanks to Google for providing a [Compose key layout for Chrome OS](https://github.com/google/extra-keyboards-for-chrome-os/tree/master/composekey) and to [gnarf/osx-compose-key](https://github.com/gnarf/osx-compose-key) for information about how to set up macOS to use a Compose key.
