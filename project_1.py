from flask import Flask, request, url_for
import random

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

personne = ''
health = 100
mushroom = 0
hatchet = 0

@app.route('/')
def hello_person():
    return """
        <body style="margin:60;padding:0">
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .yourname{
        width:640px;
        margin:0 auto;
        }
        .form1{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="yourname">What is your name?</p>
        <p class="break"> </p>
        <form class="form1" method="POST" action="%s"><input name="person" /><input type="submit" value="Continue" /></form>
        </div>
        </body>
        """ % (url_for('greet'),)

@app.route('/greet', methods=['POST'])
def greet():
    global personne
    global health
    health = 100

    personne = request.form["person"]
    greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])
    return """
        <body style="margin:60;padding:0">
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .namegreet{
        width:640px;
        margin:0 auto;
        }
        .link{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="namegreet">%s, %s!</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="break"> </p>
        <p class="link"><a href="%s">Click here to begin your journey...</a></p>
        </div>
        </body>
        """ % (greet, personne, health, url_for('intro'))

@app.route('/intro')
def intro():
    global personne
    global health
    health = health - 1

    intro = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>As you wander out of town and into the woods you're shaking your head in disbelief...
        Kicked out of yet another pub for involvement in a brawl... Nevermind the fact that
        you started it!</p>
        <p>While lost deeply in disgust and muttering to yourself you have failed to notice that
        the woods have become much thicker, the undergrowth sparse, the trees very large, and very
        little light filtering through to the path along which you are - <b>OOPS!</b> - tripping.
        <font color="red">(Health - 1)</font></p>
        <p>You pick yourself up and dust off your nether regions, pleased to note the only damage
        is to your pride. <font color="orange">(Pride - 1)</font> You glance around and see to your right what appears to be a lovely
        meadow. You leave the relative safety of the path and head toward green grass and sunshine.</p>
        <p>The meadow is not large and in the center is a flat rock approximately 4 feet in diameter. On the
        rock are two items which could be considered valuable. The first is a pile of apples - 5 or 7
        at a rough count. The other is a hatchet. Unfortunately, you are only able to carry one
        of these two items.</p>
        <p>Will you pick up the hatchet, or inspect the apples?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .player{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="player">%s,%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Pick up the hatchet.</a></p>
        <p class="link2"><a href="%s">Inspect the apples.</a></p>
        </div>
        </body>
        """ % (personne, intro, health, url_for('static', filename='option1'), url_for('static', filename='option2'))

@app.route('/static/option1')
def option1():
    global health
    global hatchet
    hatchet = hatchet + 1

    option1 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You pick up the hatchet before realizing it was lying in a pile of what could only be
        the fecal matter of some mammalian creature, perhaps <i>bos primigenius namadicus,</i> more commonly known as the
        Indian auroch. How a heap of excrement from an extinct bovine known only to have lived in south Asia before
        2000BC found its way to North America, you don't know. Maybe you're just drunk and it's merely a mass of common
        cow manure. In any case, it smells wretched and perhaps the hatchet should be cleaned before you carry on.</p>
        <p>There appears to be a river running along side the meadow. Should said river not be infested with flesh eating eels,
        it would be a great place to cleanse your newly acquired hatchet before you contract Salmonella. Alternatively, there
        is a mighty tasty looking mushroom at your feet, just begging to be consumed!</p>
        <p>Due to the effects of intense intoxification, your brain is only capable of processing one action at a time, and upon
        taking either action you will immediately forget what your other option was.</p>
        <p>How shall you proceed?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Clean the feces from the hatchet.</a></p>
        <p class="link2"><a href="%s">Consume that delicious looking mushroom.</a></p>
        """ % (option1, health, url_for('static', filename='option11'), url_for('static', filename='option12'))

@app.route('/static/option11')
def option11():
    global health
    health = health - 1
    global mushroom
    mushroom = 0

    option11 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You near the river and dip your hand and hatchet into the current to rid both of the accumulated fecal matter.</p>
        <p>Ouch. <font color="red">(Health - 1)</font> Something just nibbled your fingertip. What was that?</p>
        <p><font size="10">OH GOD, EELS!</font></p>
        <p>A group of massive, man-eating eels emerges from the river! You run for dear life as they chase you across the
        meadow.</p>
        <p>Do you run back they way you came, or do you run into the thick woods?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="asdasd">Without time to think about how eels are able to traverse land, you:</p>
        <p class="link1"><a href="%s">Run back the way you came!</a></p>
        <p class="link2"><a href="%s">Run into the woods!</a></p>
        """ % (option11, health, url_for('static', filename='option111'), url_for('static', filename='option112'))

@app.route('/static/option111')
def option111():
    global health
    health = health - 60

    option111 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You decide it's best to run back the way you came.</p>
        <p>With the giant eels in hot persuit, you run past the large rock where you found the hatchet. The pile of apples
        still sits upon it. Looking back, you notice one of the flesh-hungry eels inspecting the apples.</p>
        <p><font size="10" color="red">BOOM</font></p>
        <p>You are knocked off your feet. <font color="red">(Health - 60)</font>
        <p>Apparently there was some kind of explosive device under that pile of apples because all the giant man-eating eels
        just blew to freaking smithereens!</p>
        <p>Unfortunately, the blast has dealt quite a bit of damage to your body. The hatchet is lodged deep into your left leg
        and your foot appears to be missing. It really sucks not having both feet, but you're also losing quite a bit of blood.</p>
        <p>Should you seek medical attention or attempt to locate your missing foot?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Search for a medical facility.</a></p>
        <p class="link2"><a href="%s">Look for foot.</a></p>
        """ % (option111, health, url_for('static', filename='option121'), url_for('static', filename='option1112'))

@app.route('/static/option1112')
def option1112():
    global health
    health = health - 38

    option1112 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You crawl around on the ground in search of your missing foot. You trip and fall into the blast crater. It's walls
        are just high enough to prevent you from being able to climb out.</p>
        <p>In a pool of bloody eel remains, you slowly bleed to death from your wounds. <font color="red">(Health - 38)</font></p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="red">Health: %i</font></p>
        <p>You have died.
        The end.</p>
        """ % (option1112, health)

@app.route('/static/option112')
def option112():
    global health
    health = health - 200
    option112 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You run towards the woods but you realize that there are no woods! It's just a 70 foot concrete wall
        painted to look like trees! It's all a facade!</p>
        <p>The eels, the meadow, the town, it was all a game!
        <p>Cornered, you watch the gigantic flesh eating eels surround you. "Well, this is it," you
        say to yourself.</p>
        <p>An eel promptly bites your head off and you die. <font color="red">(Health - 200)</font></p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="red">Health: %i</font></p>
        <p>The end.</p>
        """ % (option112, health)

@app.route('/static/option12')
def option12():
    global personne
    global mushroom
    mushroom = 1
    global health
    health = health - 25

    option12 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>It tastes like the black death.</p>
        <p>You suddenly feel like your internal organs are on fire.</p>
        <p>You vomit approximately 13 times. <font color="red">(Health - 25)</font></p>
        <p>You realize that you just ate a poisonous mushroom. Why on Earth did you think
        that was a good idea?<p>
        <p>Your vision blurs. Your body aches. Is this the end?</p>
        <p>Nope, you still have like, 74 health left!</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="see">See? You're not dying, just horribly ill! What are you going to do about it?</p>
        <p class="link1"><a href="%s">Seek medical attention.</a></p>
        <p class="link2"><a href="%s">Nothing.</a></p>
        """ % (option12, health, url_for('static', filename='option121'), url_for('static', filename='option122'))

@app.route('/static/option121')
def option121():
    global health
    option121 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You stumble back into town and head in the direction of the local hospital.
        As you approach the hospital, you can see a sign hanging on the door that reads, "CLOSED."</p>
        <p>What? Since when do hospitals close?</p>
        <p>You inspect the signage above the door. Oh, it's an animal hospital.</p>
        <p>You limp your way down the street in search of the actual hospital and, lucky for you, a
        kind stranger provides you with some assistance. The stranger informs you that the real hospital
        and the animal hospital are accross the street from each other.
        <p>Three hours later, you find the actual hospital. You approach the front desk and attempt to
        describe your ailment.</p>
        <p>Everyone around you goes wide eyed and a nurse quickly ushers you into a room with a bed. After
        laying down on the bed you start to feel sleepy...
        </div>
        </body>
        """
    if mushroom == 1:
        return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link2"><a href="%s">Continue...</a></p>
        """ % (option121, health, url_for('static', filename='hosp1'))

    else:
        return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link2"><a href="%s">Continue...</a></p>
        """ % (option121, health, url_for('static', filename='hosp2'))

@app.route('/static/hosp1')
def hosp1():
    global health
    hosp1 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You wake up, unable to tell how much time has elapsed since you passed out.
        A doctor comes in to check on you, notices you have awakened, and sits down beside you. They
        say your immune system has been severely damaged, most likely due to poisoning by ingesting
        a particular type of wild mushroom, and that you also have a serious case of salmonellosis.</p>
        <p>You soon fall into a coma. You dream of strange creatures plucking you from your home, drugging
        you, and placing you in a large zoo-like pen, surrounded by high walls painted to resemble a thick forest.</p>
        <p>You awaken. The room is empty. You sluggishly attempt to stand but your legs are weak and you collapse to
        the floor. You could attempt to exit the room or just stay there and rest.</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Leave the room.</a></p>
        <p class="link2"><a href="%s">Stay and rest.</a></p>
        """ % (hosp1, health, url_for('static', filename='hosp11'), url_for('static', filename='hosp12'))

@app.route('/static/hosp11')
def hosp11():
    global health
    health = health - 201
    hosp11 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You decide to exit the room.</p>
        <p>You stand up, legs wobbly, and open the door. Outside is a large, empty corridor.
        You begin to make your way down the corridor and accidentally trip over a trash can.
        <font color="red">(Health - 1)</font></p> As you pick yourself up you hear crashing
        sounds approaching.</p>
        <p><font size="10">IT'S A GIANT EEL!</font></p>
        <p>It slithers its way towards you and promptly bites your head off.<font color="red">(Health - 200)</font></p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="red">Health: %i</font></p>
        <p>You have died. The end.
        """ % (hosp11, health)

@app.route('/static/hosp12')
def hosp12():
    global health
    health = health - 74
    hosp12 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You decide to stay and rest and climb back into the hospital bed. You can hear a noise coming
        from outside the room... Must be hospital staff going about their work.</p>
        <p>You then see a shadow pass under the door. Maybe someone is coming to check on you. Out of
        curiosity, you stand up with wobbly legs and open the door to peek outside.</p>
        <p><font size="10">IT'S A GIANT EEL!</font></p>
        <p>Terrified, you slam the door closed and lock it. The eel pounds against the door repeatedly in
        an attempt to reach you, possibly to consume your flesh!</p>
        <p>Too afraid to move, you spend the rest of your life trapped in that hospital room, until you
        eventually die of dehydration and starvation. <font color="red">(Health - 74)</font></p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="red">Health: %i</font></p>
        <p>You have died. The end.</p>
        """ % (hosp12, health)

@app.route('/static/hosp2')
def hosp2():
    global health
    health = health - 38
    hosp2 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You wake up, unable to tell how much time has elapsed since you passed out.
        A doctor comes in to check on you, notices you have awakened, and sits down beside you.
        They say you've been through hours of surgery and they had to amputate all of your limbs.
        Shocked, you attempt to shout, <i>"But only two of my limbs were damaged!"</i> But nothing
        comes out. The doctor explains that due to a bite from a particular breed of poisonous eel, you
        have also been rendered completely paralyzed.</p>
        <p>They also say that since you have no medical insurance, you will have to pay the bill by
        selling your spare organs. This may include a kidney, a lung, several feet of intestine, a few gallons of blood,
        and some brain tissue.</p>
        <p>You lie there, unable to move, unable to speak. A tear wells up in your eye.</p>
        <p>"Oh, we'll also need to take one of your eyes," the doctor adds.</p>
        <p>You spend the rest of your life paralyzed and bed-ridden, slowly being butchered until your body can no
        longer sustain life. <font color="red">(Health - 38)</font></p>
        If only you had eaten that mushroom, your life may have turned out better. Oh, well.</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="red">Health: %i</font></p>
        <p>You died. The end.</p>
        """ % (hosp2, health)

@app.route('/static/option122')
def option122():
    global health
    global mushroom
    mushroom = 1
    option122 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>Seriously? You're violently ill and you want to to nothing?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Yeah.</a></p>
        <p class="link1"><a href="%s">Okay, maybe not.</a></p>
        """ % (option122, health, url_for('static', filename='option1221'), url_for('static', filename='option121'))

@app.route('/static/option1221')
def option1221():
    global health
    health = health - 74
    option1221 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>Sigh...</p>
        <p>OK.</p>
        <p>You decide to do nothing.</p>
        <p><font size="16">You do nothing for the rest of your life until you
        literally die of boredom. THE END.</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="red">Health: ZERO</font></p>
        """ % (option1221)

@app.route('/static/option2')
def option2():
    global personne
    global health
    health = health - 8923487925

    option2 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <font size="24" color="red">SURPRISE PIPE BOMB!</font>
        <p>You explode into a thousand pieces.</p>
        </div>
        </body>
        """
    return """
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>%s</p>
        <p class ="healthval"><font color="red">Health: %i</font></p>
        <p>Nice going, %s.</p>
        </div>
        """ % (option2, health, personne)

@app.route('/static/blinded')
def intro():
    global personne
    global health
    health = health - 1

    intro = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>Your vision starts to fade, and your sense of balance fades with it.
        You feel yourself  fall backward, however this feeling of free falling 
        persists for what seems like hours. Sounds of ethereal screams, 
        ghostly beckoning calls, and low droning hum surround you with no 
        discernible origin. </p>
        <p>All of a sudden your knees abruptly meet a rough solid ground the 
        otherworldly sound disappear but your vision does not return. A cold wet 
        something caresses your left ear and you stumble away from it frightened. 
        As you begin to stand your head us tugged backward and your vision returns. 
        The light is blinding but you see a dark amorphous shape at your feet, you 
        can feel your heart beat through your neck.</p>
        <p>Finally everything comes into focus and a sense of relief comes over you, 
        as you realize the dark shape was a happy pair of chocolate labrador pups. 
        your party increases by two.</p>
        <p>As you scan your surroundings you see a group of naked mole rats singing 
        in a southern gospel choir singing joyful hymns and a cache of crystal gems. 
        o09The gems call to you with a ominous aura, however the choir is unfamiliar 
        and gives you a strange vibe. Which do you choose to investigate?</p>
        <p>Will you inspect the gems, or walk toward the choir?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .player{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="player">%s,%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Inpect the gems.</a></p>
        <p class="link2"><a href="%s">Walk toward the choir.</a></p>
        </div>
        </body>
        """ % (personne, intro, health, url_for('static', filename='gem'), url_for('static', filename='choir'))

@app.route('/static/gem')
def intro():
    global personne
    global health
    health = health - 1

    intro = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You walk toward the gems, one in particular catches your eye. 
        It is an exquisite iridescent stone primarily black with flecks 
        of electric blues, fiery reds, and fuchsia. You hastily grab the 
        stone and instantly your vitality is instantly restored. </p>
        <p>Your sense of hearing is heightened and you hear what sounds 
        like a string being pulled coming from behind you. You feel a 
        gaze burning a hole on the back of your head. </p>
        <p>An overwhelming feeling of dread showers over you.</p>
        <p>You must make a split second decision, do you choose to turn 
        to face the sound or tuck your head between your knees?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .player{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="player">%s,%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Turn and face the sound.</a></p>
        <p class="link2"><a href="%s">Duck and run.</a></p>
        </div>
        </body>
        """ % (personne, intro, health, url_for('static', filename='turn'), url_for('static', filename='bear_trap'))

@app.route('/static/choir')
def intro():
    global personne
    global health
    health = health - 1

    intro = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>As you approach the heavenly singing, you see that the vocalists 
        are not actually naked mole rats at all. Their skin hangs loosely 
        in excess moving with the wind, their eyes are but vertical slits, 
        bodies nude entirely hairless. They look ancient, free from shame, 
        with indistinguishable genders. They stand in the ruins of an 
        amphitheater, painted walls with crawling vines of ivy and moss that 
        mark the eons that have passed.</p>
        <p>The singing stops jarringly, you have spent so much time admiring 
        the performance that you have not payed attention to the other 
        surroundings. The audience as well as the singers stare at you. 
        A compelling force drives you to move toward the stage.</p>
        <p>You find yourself standing before large crater filled with human 
        bones. A bass speaks with the sound of a rolling thunder, ’The fates 
        have given us another sacrifice, it is time to feast siblings.’ 
        Creatures tear you apart while you stand helpless and succumb to 
        this brutal end.</p>
        </div>
        </body>
        """
     % (personne, intro, health,)

@app.route('/static/turn')
def intro():
    global personne
    global health
    health = health - 1

    intro = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>Just as soon as you turn your head you are blown back by a force 
        that blinds you. Trying to breathe you notice a sweet taste in your 
        mouth. You reach for your face and realize you were struck with a pie. 
        he feeling of dread is now replaced with embarrassment as children 
        stand near you laughing.</p>
        <p>Though your face is coated in custard and cream you feel glad 
        that your decision was not made impulsively.</p>
        <p>One of the older children extends you her hand, and offers to 
        bring you to her village, where you can find a warm meal and shelter. 
        Her smile is warm but you are wary as they just made of 
        fool of you. </p>
        <p>Do you accept the offer or find your own way?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .player{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="player">%s,%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Accept her offer.</a></p>
        <p class="link2"><a href="%s">Find your own way.</a></p>
        </div>
        </body>
        """ % (personne, intro, health, url_for('static', filename='offer'), url_for('static', filename='own_way'))

@app.route('/static/bear_trap')
def intro():
    global personne
    global health
    health = health - 1

    intro = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p>You duck and hear a whoosh pass over you. 
        You get up and run away but trip and your 
        head falls into a bear trap you are certainly dead. </p>
        </div>
        </body>
        """ % (personne, intro, health,)


if __name__ == '__main__':
    app.run()
