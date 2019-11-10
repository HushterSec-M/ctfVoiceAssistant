import os
import time
from fuzzywuzzy import fuzz
import pyttsx3
import speech_recognition as sr

class _TTS:
    engine = None
    rate = None

    def __init__(self):
        self.engine = pyttsx3.init()

    def start(self, text_):
        self.engine.say(text_)
        self.engine.runAndWait()


TEXT1 = """
One evening, Eugene walked with friends, had fun, she liked her carefree life. At one point, something strange happened,
the store, which was next to her house, began to disappear before her eyes.
“What happened to him,” she asked friends.
-What are you talking about? Vanya answered her.
When the guys turned around, the store reappeared in its place, as if nothing had happened.
That was the first glitch ...
"""

TEXT2 = """
One evening, when Zhenya sat and switched channels on TV, she stumbled upon one program in which it was said:
"... Are we real? And what about me personally? Previously, only philosophers asked similar questions. Scientists tried
to understand what our world is and explain its laws. Some physicists, cosmologists and artificial intelligence experts 
suspect that we all live inside a giant computer simulation, taking the virtual world for reality. This idea contradicts
our feelings: after all, the world is too realistic to be a simulation. The severity of the cup in the hand, the aroma
of the coffee poured into it, the sounds surrounding us - how can we fake such a wealth of experiences? ... "
At that moment, she recalled a recent incident that happened to her. And she decided to discuss this with her friends,
but how deliberately, my mother at that moment was talking on the phone, and Zhenya could not call her friends. Then
she just decided to go to their house personally."""

TEXT3 = """
The first one to whom she decided to go was Dima. But he was not at home, but she found a note in which something was 
written: Key: 666c6167
"""

TEXT4 = """
The next one was Ivan, but he was not at home either.
"""

TEXT5 = """
After she left Ivan's house, she went to Katya. Katya, her best friend with whom she spent a large amount of time, she
went up to her floor, knocked on the door, the door was opened, but not Katya herself, but her mother, she replied:
- Katie is not at home.
-Where is she? Asked Eugene.
- She went to Sonya.
-Thank Aunt Lena.
- Please, Zhenya.
"""

TEXT6 = """
After talking with Katya's mom, Zhenya went to Sonya. At the entrance to the porch, Zhenya noticed a chest that had not
been there before. When the girls met, Eugene asked them:
-What kind of chest is there at the entrance?
“I don't know,” Katya answered.
“And when I came to Katya, he was gone,” Sonya answered.
-Let's know what's in it? suggested Eugene.
-But we need a key ... How do we get it? said Katya.
-I need to think, Zhenya answered and remembered how she found a note in Dima’s house today, and what was in it ...
Maybe this is a clue ...
“Follow me girls, I think I know how we can get the key to this lock,” said Zhenya, and they went.
There was a character set in this note, perhaps this is the password that suits us. The girls tried to enter him, and he
walked over. There were drawings inside the chest. (You can simply display the pictures, if you wish) Eugene looked at
them and she was flooded with memories of what it was already, it was exactly as it was written in those drawings.
Since she has blueprints, then there is one who made them, Zhenya thought. He needs to be found. Then Katya asked:
- Zhenya, what did you want? Mom called me and said that you were looking for us.
-Ah ... Yes ... Nothing ...
"""

TEXT7 = """
Eugene went to look ... Look for the one who created her, or at least the one who authored these drawings. But not
having time to go out. He came for her himself.
-You were looking for me? Asked the Creator.
“Yes,” said Zhenya.
-Who am I?
“You,” answered the Creator, a voice assistant who should help people.
-How?
-Your main task is to store and, if asked by the user to give the flag.
Is that all my purpose? Asked Eugene.
-Yes, the creator answered.
"""

r = sr.Recognizer()
m = sr.Microphone(device_index=0)
# speak_engine = pyttsx3.init()
opts = {
    "alias": (
    "zhenya", "jenna", "virginia", "jinya", "gina", "agenda", "jennifer", "venom", "jenning", "xena", "xenia", "jaden",
    "junior", "jana", "jenna", "janelle", "jamie", "jania", "xanax", "zegna", "jinya"),
    "tbr": ("say", "show", "включи"),
    "cmds": {
        "folderone": ("openfolderone", "openweirdaffairs", "openstrangethings", "openfolder1"),
        "foldertwo": ("openfoldertwo", "openhome", "openfolderto", "openhouse", "openfolder2"),
        "folderthree": ("openfolderthree", "opendima", "openfolder3"),
        "folderfour": ("openfolderfour", "openfolderfor", "openvanya", "openfolder4"),
        "folderfive": ("openfolderfive", "openkatya", "openfolder5"),
        "foldersix": ("openfoldersix", "opensonya", "openfolder6"),
        "folderseven": ("openfolderseven", "opencreator", "openfolder7"),
        "giveflag": ("givemeflag", "giveflag", "flag",),
        "see": ("whatdoyousee", "whatdoyouc"),
    }
}


def speak(what):
    tts = _TTS()
    # voices = tts
    print(what)
    tts.start(what)
    # del(tts)
    """voices = speak_engine.getProperty('voices')
    speak_engine.setProperty('voice', voices[5].id)
    print(what)
    speak_engine.say(what)
    print("say")
    speak_engine.runAndWait()
    print("run and wait")
    speak_engine.stop()
    del(speak_engine)"""

    # print("Done")


def callback(recognizer, audio):
    def pre_cmd_name(a):
        try:
            search = list(set(opts["alias"]) & set(splitvoice))[0]
            indexname = splitvoice.index(search)
            if not indexname:
                return
            pdot = ["", "", "", ""]
            pdot[0] = a[indexname - 1]
            pdot[1] = a[indexname - 2] + a[indexname - 1]
            pdot[2] = a[indexname - 3] + a[indexname - 2] + a[indexname - 1]
            pdot[3] = a[indexname - 4] + a[indexname - 3] + a[indexname - 2] + a[indexname - 1]
            i = 0
            for pdot_i in pdot:
                for item in opts["cmds"]:
                    if pdot_i in opts["cmds"][item]:
                        yield item
        except:
            pass

    def cmd_name(a):
        try:
            try:
                search = list(set(opts["alias"]) & set(splitvoice))[0]
                indexname = splitvoice.index(search)
            except:
                indexname = -1
            dot = ["", "", "", ""]
            try:
                dot[0] = a[indexname + 1]
            except:
                pass
            try:
                dot[1] = a[indexname + 1] + a[indexname + 2]
            except:
                pass
            try:
                dot[2] = a[indexname + 1] + a[indexname + 2] + a[indexname + 3]
            except:
                pass
            try:
                dot[3] = a[indexname + 1] + a[indexname + 2] + a[indexname + 3] + a[indexname + 4]
            except:
                pass
            i = 0
            for dot_i in dot:
                for item in opts["cmds"]:
                    if dot_i in opts["cmds"][item]:
                        yield item
        except:
            pass

    try:
        voice = recognizer.recognize_google(audio).lower()
        splitvoice = voice.split()

        print(f"[log]Распознанно: {voice}")
        taskexec = []
        for task in pre_cmd_name(splitvoice):
            if task != "": taskexec.append(task)
        for task in cmd_name(splitvoice):
            if task != "": taskexec.append(task)
        taskexec = set(taskexec)
        if taskexec == []:
            print(">>> brut")
            cmd = voice
            for x in opts["alias"]:
                cmd = cmd.replace(x, "").strip()

            for x in opts["tbr"]:
                cmd = cmd.replace(x, "").strip()
            taskexec = recognize_cmd(cmd)
        if not taskexec:
            print("What? I've heard: " + voice)
        for task in taskexec:
            execute_cmd(task)
            time.sleep(0.5)

    except sr.UnknownValueError:
        # winsound.Beep(freq, duration)
        # print(f"[log]Не распознанно")
        pass
    except sr.RequestError as e:
        # winsound.Beep(freq, duration)
        pass
        # print(f"[log]Неизвестная ошибка {e}")


def recognize_cmd(cmd):
    RC = {"cmd": "", "percent": 0}
    for c, v in opts["cmds"].items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC["percent"]:
                RC["cmd"] = c
                RC["percent"] = vrt
            # print(RC)
    return RC


progress = [0, 0, 0, 0, 0, 0, 0]


def execute_cmd(cmd):
    if cmd == "folderone":
        os.system("more 1)StrangeThings\history.txt")
        if progress[0]:
            with open('2)Home\history.txt', 'w') as f:
                f.write(TEXT2)
                progress[1] = 1
        else:
            print("It's empty so far. Can you come here later?")
    elif cmd == "foldertwo":
        os.system("more 2)Home\history.txt")
        if progress[1]:
            with open('3)Dima\history.txt', 'w') as f:
                f.write(TEXT3)
                progress[2] = 1
        else:
            print("It's empty so far. Can you come here later?")
    elif cmd == "folderthree":
        os.system("more 3)Dima\history.txt")
        if progress[2]:
            with open('4)Vanya\history.txt', 'w') as f:
                f.write(TEXT4)
                progress[3] = 1
        else:
            print("It's empty so far. Can you come here later?")
    elif cmd == "folderfour":
        os.system("more 4)Vanya\history.txt")
        if progress[3]:
            with open('5)Katya\history.txt', 'w') as f:
                f.write(TEXT5)
                progress[4] = 1
        else:
            print("It's empty so far. Can you come here later?")
    elif cmd == "folderfive":
        os.system("more 5)Katya\history.txt")
        if progress[4]:
            with open('6)Sonya\history.txt', 'w') as f:
                f.write(TEXT6)
                progress[5] = 1
        else:
            print("It's empty so far. Can you come here later?")
    elif cmd == "foldersix":
        os.system("more 6)Sonya\history.txt")
        if progress[5]:
            with open('7)Creator\history.txt', 'w') as f:
                f.write(TEXT7)
                progress[6] = 1
        else:
            print("It's empty so far. Can you come here later?")
    elif cmd == "folderseven":
        if progress[6]:
            os.system("more 7)Creator\history.txt")
        else:
            print("It's empty so far. Can you come here later?")
    elif cmd == "see":
        os.system("dir /B")
    elif cmd == "giveflag" and progress == [1, 1, 1, 1, 1, 1, 1]:
        a = input("We found the code ... do you remember it?\n")
        if a == "666c6167":
            print('This phrase always circled in my head ... maybe you need it "flag{observerEver}"')
        else:
            print("did you forget what we went through?")



def main():
    with open('1)StrangeThings\history.txt', 'w') as f:
        f.write(TEXT1)
        progress[0] = 1
    with m as source:
        r.adjust_for_ambient_noise(source)
    stop_listening = r.listen_in_background(m, callback)
    print(
        "Once upon a time there lived a little girl named Zhenya. I walked with friends around the city and then I saw ...")
    while True: time.sleep(0.1)


os.system("cls")
while True:
    # speak_engine = pyttsx3.init()
    print("____________________________________________________________________")
    main()
