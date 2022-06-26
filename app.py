import cohere
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate_title', methods=["POST"])
def generate_titles():
    global youtube_tags
    youtube_tags = request.form.get("youtube_tags_text_area")
    if youtube_tags =="":
        return render_template("index.html")
    prediction = callCohereAPI(youtube_tags)
    youtube_title = prediction.generations[0].text
    youtube_title = youtube_title[:-2]
    return render_template("generate_title.html",title=youtube_title)

@app.route('/generate_again')
def generate_again():
    if youtube_tags!=None:
        prediction = callCohereAPI(youtube_tags)
        youtube_title = prediction.generations[0].text
        youtube_title = youtube_title[:-2]
        return render_template("generate_title.html", title=youtube_title)
    else:
        return render_template("index.html")

def callCohereAPI(tags):
    co = cohere.Client('RkghRbPkKZAzCMGfaP5H3Ab6qpOBSkhlQMqN24CB')
    pred = co.generate(
        model='large',
        prompt='\nThis is a bot that generates a YouTube video title based on its tags:\nTags: i build 10 automatic farms to change my hardcore world forever,notnotbrock,notnotbrock hardcore,1.18 hardcore,hardcore lets play,minecraft lets play,sandiction,sandiction hardcore,wadzee,wadzee hardcore,sandiction end island,loony,loony hardcore,the loony adventure,sandiction every mob,minecraft,but,hardcore,yeahjaron 100 by 100,minecraft hardcore,i survived 100 days,i survived 1000 days,i survived 500 days,wadzee starting over,notnotbrock hardcore series,bean\nTitle: I Built 10 INSANE AUTOMATIC Farms in Minecraft Hardcore (#7)\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: i built an underground mega base in minecraft hardcore,notnotbrock,notnotbrock hardcore,1.18 hardcore,hardcore lets play,minecraft lets play,sandiction,sandiction hardcore,wadzee,wadzee hardcore,sandiction end island,loony,loony hardcore,the loony adventure,sandiction every mob,minecraft,but,hardcore,minecraft hardcore,minecraft hardcore lets play,i survived 100 days,i survived 1000 days,i survived 500 days,wadzee starting over,notnotbrock hardcore series,cool\nTitle: I Built an Underground MEGA BASE in Minecraft Hardcore (#6)\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: Minecraft,Maizen\nTitle: Minecraft Jailbreak - Escape the Prison\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: TheDooo,Dooo,Funny Gaming Moments,playing guitar on omegle,gta 5,gta 5 mods,grand theft auto,gta 5 mod,gta 5 online,grand theft auto v,grand theft auto 5,gta,gta v,gta v online,gta race,gta 5 races,gta v races,gta online,gta 5 funny moments,gta 5 sumo,gta 5 mods pc\nTitle: click on this video or my mom gets it\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: funny gaming moments,r6 funny moments,r6 funtage,rainbow six siege update,r6 update,r6 siege,rainbow six siege new operators,rainbow six siege funny moments,rainbow six siege funtage,r6 new operator,rainbow six burnt horizon,rainbow six siege gridlock,rainbow six siege hacker,hacking funny moments,gaming hacker,r6 hacker,r6 memes,rainbow six siege memes,r6 glitch,rainbow six glitches,rainbow six siege tips\nTitle: When a HACKER Plays Rainbow Six Siege\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: Title: goofy ahh memes \n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: stand up,stand up comedy,comedy central stand up,comedy,comedian,comedians,pride,lgbt,lgbtq,lgbtq comedians,gay,lesbian,bisexual,transgender,queer,queer comedians,gay comedians,lesbian comedians,jaboukie young white,sabrina jalees,bob the drag queen,joel kim booster,Sydnee Washington,pat regan,paris sashay,Solomon georgio,dewayne perkins,funny video,comedy videos,jokes,funny jokes,funny clips,laugh,humor,best comedy,best stand up\nTitle: 9 LGBTQ+ Stand-Up Comedians You Should Know\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: Title: stand up comedy pt 02 | tiktok compilation\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: Title: stand up comedy pt 03 | tiktok compilation\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: dank,dank memes,dank memes compilation,dankest memes,meme compilation,dankest memes compilation,try not to laugh,try not to laugh challenge,memes,meme,funny,funny videos,ylyl,you laugh you lose,tntl,you laugh you lose challenge,funny memes,best memes,memes compilation,tik tok memes,memes that,dank compilation,memesheep,best memes compilation,memes 2021,fortnite memes,memerman,unusual memes,we have memes,memes for you,Memes,funny memes compilation\nTitle: come, we have funny memes for you\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: grand theft auto v,gta,gtav,grand theft auto,meme,memes,british,british memes,grand theft auto british\nTitle: But I did kidnap his wife but British\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: dank,dank memes,dank memes compilation,dankest memes,meme compilation,dankest memes compilation,try not to laugh,try not to laugh challenge,memes,meme,funny,funny videos,ylyl,you laugh you lose,tntl,you laugh you lose challenge,funny memes,best memes,memes compilation,tik tok memes,memes that,dank compilation,memesheep,best memes compilation,memes 2021,fortnite memes,memerman,unusual memes,unusual videos,you laugh,memes but if you laugh,memes but\nTitle: memes but if you laugh, he\'s coming for you\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags: henry stickmin,henry stickman,henry stickmin collection,henry stickmin easter eggs,henry stickmin secrets,henry stickmin references,henry stickmin achievements,easter eggs,secrets,references,henry stickmin all references,list of references,phoenix wright,half life,minecraft,matrix,super mario,sonic,pokemon,gta,tf2,fallout,street fighter,garrys mod,skyrim,metal gear solid,hitman,kacpi26\nTitle: Henry Stickmin All Easter Eggs, Secrets And References\n--\nThis is a bot that generates a YouTube video title based on its tags:\nTags:'+tags+'Title:',
        max_tokens=20,
        temperature=0.7,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
    return pred


youtube_tags = None
if __name__ == '__main__':
    app.run()
