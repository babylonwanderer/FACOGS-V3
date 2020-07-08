import discord
from redbot.core import commands
from random import choice
from typing import List

rules: List[str] = [
    _(1:  "Once you have their money, never give it back.."),
    _(2:  "You can't cheat an honest customer, but it never hurts to try.."),
    _(3:  "Never spend more for an acquisition than you have to.."),
    _(4:  "Sex and profit are the two things that never last long enough.."),
    _(5:  "If you can't break a contract, bend it."),
    _(6:  "Never let family stand in the way of opportunity."),
    _(7:  "Always keep you ears open."),
    _(8:  "Keep count of your change."),
    _(9:  "Instinct plus opportunity equals profit."),
    _(10:  "A dead customer can't buy as much as a live one."),
    _(11:  "Latinum isn't the only thing that shines."),
    _(12:  "Anything worth selling is worth selling twice."),
    _(13:  "Anything worth doing is worth doing for money."),
    _(14:  "Anything stolen is pure profit."),
    _(15:  "Acting stupid is often smart."),
    _(16:  "A deal is a deal ... until a better one comes along."),
    _(17:  "A bargain usually isn't."),
    _(18:  "A Ferengi without profit is no Ferengi at all."),
    _(19:  "Don't lie too soon after a promotion."),
    _(20:  "When the customer is sweating, turn up the heat."),
    _(21:  "Never place friend ship before profit."),
    _(22:  "Wise men can hear profit in the wind."),
    _(23:  "Never take the last coin, but be sure to get the rest."),
    _(24:  "Never ask when you can take."),
    _(25:  "Fear makes a good business partner."),
    _(26:  "The vast majority of the rich in this galaxy did not inherit their wealth; they stole it."),
    _(27:  "The most beautiful thing about a tree is what you do with it after you cut it down."),
    _(28:  "Morality is always defined by those in power."),
    _(29:  "When someone says `It's not the money`, they're lying."),
    _(30:  "Talk is cheap; synthehol costs money."),
    _(31:  "Never make fun of a Ferengi's mother."),
    _(32:  "Be careful what you sell. It may do exactly what the customer expects."),
    _(33:  "It never hurts to suck up to the boss."),
    _(34:  "War is good for business."),
    _(35:  "Peace is good for business."),
    _(36:  "Too many Ferengi can't laugh at themselves anymore."),
    _(37:  "You can always buy back a lost reputation."),
    _(38:  "Free advertising is cheap."),
    _(39:  "Praise is cheap. Heap it generously on all customers."),
    _(40:  "If you see profit on a journey, take it.."),
    _(41:  "Money talks, but having a lots of it gets more attention.."),
    _(42:  "Only negotiate when you are certain to profit."),
    _(43:  "Caressing an ear is often more forceful than pointing a weapon."),
    _(44:  "Never argue with a loaded phaser."),
    _(45:  "Profit has limits. Loss has none."),
    _(46:  "Labor camps are full of people who trusted the wrong person."),
    _(47:  "Never trust a man wearing a better suit than you own."),
    _(48:  "The bigger the smile, the sharper the knife."),
    _(49:  "Old age and greed will always overcome youth and talent."),
    _(50:  "Never bluff a Klingon."),
    _(51:  "Never admit a mistake if there's someone else to blame."),
    _(52:  "Only Bugsy could have built Las Vegas."),
    _(53:  "Sell first; ask questions later."),
    _(54:  "Never buy anything you can't sell."),
    _(55:  "Always sell at the highest possible profit."),
    _(56:  "Pursue profit; women come later."),
    _(57:  "Good customers are almost as rare as Latinum - treasure them."),
    _(58:  "Friendship is seldom cheap."),
    _(59:  "Fee advice is never cheap.",
    _(60:  "Never use Latinum where your words will do."),
    _(61:  "Never buy what can be stolen."),
    _(62:  "The riskier the road, the greater the profit."),
    _(63:  "Power without profit is like a ship without an engine."),
    _(64:  "Don't talk shop; talk shopping."),
    _(65:  "Don't talk ship; talk shipping."),
    _(66:  "Anyone serving in a fleet who is crazy can be relieved, if they ask for it."),
    _(67:  "Enough is never enough."),
    _(68:  "Compassion is no substitute for a profit."),
    _(69:  "You could afford your ship without your government - if it weren't for your government."),
    _(70:  "Get the money first, then let the buyers worry about collecting the merchandise."),
    _(71:  "Gamble and trade have two things in common: risk and Latinum."),
    _(72:  "Never let the competition know, what you're thinking."),
    _(73:  "Never trust advice from a dying Ferengi; listen but don't trust."),
    _(74:  "A Ferengi without profit is no Ferengi at all."),
    _(75:  "Home is where the heart is, but the stars are made of Latinum."),
    _(76:  "Every once in a while, declare peace. It confuses the hell out of your enemies."),
    _(77:  "Go where no Ferengi has gone before; where there is no reputation there is profit."),
    _(78:  "Don't discriminate. The most unlikely species can create the best customers."),
    _(79:  "Benefit from the Vulcan greed for knowledge."),
    _(80:  "If it works, sell it. If it works well, sell it for more. If it doesn't work, quadruple the price and sell it as an antique."),
    _(81:  "There's nothing more dangerous than an honest businessman."),
    _(82:  "A smart customer is not a good customer."),
    _(83:  "Revenge is profitless."),
    _(84:  "She can touch your ears but never your Latinum."),
    _(85:  "Death takes no bribes."),
    _(86:  "A wife is a luxury, a smart accountant a necessity."),
    _(87:  "Trust is the biggest liability of all."),
    _(88:  "When the boss comes to dinner, it never hurts to have the wife wear something."),
    _(89:  "Latinum lasts longer than lust."),
    _(90:  "Mine is better than ours."),
    _(91:  "He who drinks fast pays slow."),
    _(92:  "Never confuse wisdom with luck."),
    _(93:  "He's a fool who makes his doctor his heir."),
    _(94:  "Beware of small expenses: a small leak will kill a ship."),
    _(95:  "Important, more impotant, Latinum."),
    _(96:  "Faith moves mountains - of inventory."),
    _(97:  "If you would keep a secret from an enemy, don't tell it to a friend."),
    _(98:  "Profit is the better part of valor."),
    _(99:  "Never trust a wise man."),
    _(100:  "Everything that has no owner, needs one."),
    _(101:  "Never do something you can make someone do for you."),
    _(102:  "Nature decays, but Latinum lasts forever."),
    _(103:  "Sleep can interfere with opportunity."),
    _(104:  "Money is never made. It is merely won or lost."),
    _(105:  "Wise men don't lie, they just bend the truth."),
    _(106:  "There is no honor in poverty."),
    _(107:  "Win or lose, there's always Huyperian Beetle Snuff."),
    _(108:  "A woman wearing clothes is like a man without profit."),
    _(109:  "Dignity and an empty sack is worth the sack."),
    _(110:  "Only a fool passes up a business opportunity."),
    _(111:  "Treat people in your debt like family ... exploit them."),
    _(112:  "Never sleep with the boss's wife unless you pay him first."),
    _(113:  "Never sleep with the boss's sister."),
    _(114:  "Small print lead to large risk."),
    _(115:  "Greed is eternal."),
    _(116:  "There's always a way out."),
    _(117:  "If the profit seems too good to be true, it usually is."),
    _(118:  "Never cheat a honest man offering a decent price."),
    _(119:  "Buy, sell, or get out of the way."),
    _(120:  "Even a blind man can recognize the glow of Latinum."),
    _(121:  "Everything is for sale, even friendship."),
    _(122:  "As the customers go, so goes the wise profiteer."),
    _(123:  "A friend is only a friend until you sell him something. Then he is a customer."),
    _(124:  "Friendship is temporary, profit is forever."),
    _(125:  "A lie isn't a lie until someone else knows the truth."),
    _(126:  "A lie isn't a lie, it's just the truth seen from a different point of view."),
    _(127:  "Gratitude can bring on generosity."),
    _(128:  "Ferengi are not responsible for the stupidity of other races."),
    _(129:  "Never trust your customers."),
    _(130:  "Never trust a beneficiary."),
    _(131:  "If it gets you profit, sell your own mother."),
    _(132:  "The flimsier the produce, the higher the price."),
    _(133:  "Never judge a customer by the size of his wallet ... sometimes good things come in small packages."),
    _(134:  "There's always a catch."),
    _(135:  "The only value of a collectible is what you can get somebody else to pay for it."),
    _(136:  "The sharp knife cuts quickly. Act without delay!."),
    _(137:  "Necessity is the mother of invention. Profit is the father."),
    _(138:  "Law makes everyone equal, but justice goes to the highest bidder."),
    _(139:  "Wives serve; brothers inherit."),
    _(140:  "The answer to quick and easy profit is: buy for less, sell for more."),
    _(141:  "Competition and fair play are mutually exclusive. Fair play and financial loss go hand-in-hand."),
    _(142:  "A Ferengi waits to bid until his opponents have exhausted themselves."),
    _(143:  "The family of Fools is ancient."),
    _(144:  "There's nothing wrong with charity ... as long as it winds up in your pocket."),
    _(145:  "Always ask for the costs first."),
    _(146:  "If possible sell neither the sizzle nor the steak, but the Elphasian wheat germ."),
    _(147:  "New customers are like razor toothed gree worms. They can be succulent, but sometimes they bite back."),
    _(148:  "Opportunity waits for no one."),
    _(149:  "Females and finances don't mix."),
    _(150:  "Make your shop easy to find."),
    _(151:  "Sometimes, what you get free costs entirely too much."),
    _(152:  "Ask not what your profits can do for you; ask what you can do for your profits."),
    _(153:  "You can't free a fish from water."),
    _(154:  "The difference between manure and Latinum is commerece."),
    _(155:  "What's mine is mine, and what's yours is mine too."),
    _(156:  "Even in the worst of times someone turns a profit."),
    _(157:  "You are surrounded by opportunities; you just have to know where to look."),
    _(158:  "Don't pay until you have the goods.",
    _(159:  "The customer is always right ... until you have their cash."),
    _(160:  "Respect is good, Latinum is better."),
    _(161:  "Never kill a customer, unless you make more profit out of his death than out of his life."),
    _(162:  "His money is only your's when he can't get it back."),
    _(163:  "A thirsty customer is good for profit, a drunk one isn't."),
    _(164:  "Never spend your own money when you can spend someone elses."),
    _(165:  "Never allow one's culture's law to get in the way of a universal goal: profit."),
    _(166:  "Never give away for free what can be sold."),
    _(167:  "If a deal is fairly and lawfully made, then seeking revenge especially unprofitable revenge, is illegal."),
    _(168:  "Beware of relatives bearing gifts."),
    _(169:  "If you're going to have to endure, make yourself comfortable."),
    _(170:  "Never gamble with an empath."),
    _(171:  "Time is Latinum. The early Ferengi get the Latinum."),
    _(172:  "If you can sell it, don't hesitate to steal it."),
    _(173:  "A piece of Latinum in the hand is worth two in a customer's pocket."),
    _(174:  "Share and perish."),
    _(175:  "When everything fails - run."),
    _(176:  "Ferengi's don't give promotional gifts!."),
    _(177:  "Know your enemies ... but do business with them always."),
    _(178:  "The world is a stage - don't forget to demand admission."),
    _(179:  "Whenever you think that things can't get worse, the FCA will be knocking on you door."),
    _(180:  "Never offer a confession when a bribe will do."),
    _(181:  "Even dishonesty can't tarnish the glow of Latinum."),
    _(182:  "Whenever you're being asked if you are god, the right answer is YES."),
    _(183:  "Genius without opportunity is like Latinum in the mine."),
    _(184:  "There are three things you must not talk to aliens: sex, religion and taxes."),
    _(185:  "If you want to ruin yourself there are three known ways: Gambling is the fastest, women are the sweetest, and banks are the most reliable way"),
    _(186:  "There are two things that will catch up with you for sure: death and taxes."),
    _(187:  "If your dancing partner wants to lead at all costs, let her have her own way and ask another one to dance."),
    _(188:  "Never bet on a race you haven't fixed."),
    _(189:  "Borrow on a handshake; lend in writing."),
    _(190:  "Drive your business or it will drive you."),
    _(191:  "Let other keep their reputation. You keep their money."),
    _(192:  "If the flushing isn't strong enough, use your brain and try the brush."),
    _(193:  "Klingon women don't dance tango."),
    _(194:  "It's always good business to know about new customers before they walk in your door."),
    _(195:  "Wounds heal, but debt is forever"),
    _(196:  "Only give money to people you know you can steal from."),
    _(197:  "Never trust your customers, especially if they are your relatives."),
    _(198:  "Employees are the rungs on your ladder to success - don't hesitate to step on them."),
    _(199:  "The secret of one person is another person's opportunity."),
    _(200:  "A madman with Latinum means profit without return."),
    _(201:  "The justification for profit is profit."),
    _(202:  "a)  A friend in need is a customer in the making"
          "b)  A friend in need means three times the profit."),
    _(203:  "A Ferengi in need, will never do anything for free."),
    _(204:  "When the Grand Nagus arrives to offer you a business opportunity, it's time to leave town until he's gone."),
    _(205:  "When the customer dies, the money stops a-comin'."),
    _(206:  "Fighting with Klingons is like gambling with Cardassians - it's good to have a friend around when you lose."),
    _(207:  "Never trust a hardworking employee."),
    _(208:  "Give someone a fish, you feed him for one day:  Teach him how to fish, and you lose a steady customer."),
    _(209:  "Tell them what they want to hear."),
    _(210:  "A wife, who is able to clean, saves the cleaning lady."),
    _(211:  "In business deals, a disruptor can be almost as important as a calculator."),
    _(212:  "If they accept your first offer, you either asked too little or offered too much."),
    _(213:  "Stay neutral in conflicts so that you can sell supplies to both sides."),
    _(214:  "Never begin a business transaction on an empty stomach."),
    _(215:  "Instinct without opportunity is useless."),
    _(216:  "Never take hospitality from someone worse off than yourself."),
    _(217:  "Only pay for it if you are confronted with loaded phaser."),
    _(218:  "Always know what you're buying."),
    _(219:  "A friend is not a friend if he asks for a discount.",
    _(220:  "Profit is like a bed of roses - a few thorns are inevitable."),
    _(221:  "Beware of any man who thinks with his lobes."),
    _(222:  "Knowledge is Latinum."),
    _(223:  "Rich men don't come to buy; they come to take."),
    _(224:  "Never throw anything away: It may be worht a lot of Latinum some Stardate."),
    _(225:  "Pride comes before a loss."),
    _(226:  "Don't take your family for granted, only their Latinum."),
    _(227:  "Loyalty can be bought ... and sold."),
    _(228:  "All things come to those who wait, even Latinum."),
    _(229:  "Beware the man who doesn't make time for oo-mox."),
    _(230:  "Manipulation may be a Ferengi's greatest tool, and liability."),
    _(231:  "If you steal it, make sure it has a warranty."),
    _(232:  "Life's no fair (How else would you turn a profit?)."),
    _(233:  "Every dark cloud has a Latinum lining."),
    _(234:  "Never deal with beggars; it's bad for profits."),
    _(235:  "Don't trust anyone who trusts you."),
    _(236:  "You can't buy fate."),
    _(237:  "There's a sucker born every minute:  Be sure you're the first to find each one."),
    _(238:  "The truth will cost."),
    _(239:  "Ambition knows no family."),
    _(240:  "The higher you bid, the more customers you drive away."),
    _(241:  "Never underestimate the inportance of the fist impression."),
    _(242:  "More is good, all is better."),
    _(243:  "If you got something nice to say, then SHOUT."),
    _(244:  "If you can't sell it, sit on it, but never give it away."),
    _(245:  "A warranty is valid only if they can find you."),
    _(246:  "He that speaks ill of the wares will buy them."),
    _(247:  "Never question luck."),
    _(248:  "Celebrate when you are paid, not, when you are promised."),
    _(249:  "Respect other culture's beliefs; they'll be more likely to give you money."),
    _(250:  "A dead vendor doesn't demand money."),
    _(251:  "Satisfaction is not guaranteed."),
    _(252:  "Let the buyer beware."),
    _(253:  "A contract without fine print is a fool's document."),
    _(254:  "Anyone who can't tell a fake doesn't deserve the real thing."),
    _(255:  "A warranty without loop-holes is a liability."),
    _(256:  "Synthehol is the lubricant of choice for a customer's stuck purse."),
    _(257:  "Only fools negotiate with their own money."),
    _(258:  "A Ferengi is only as important as the amount of Latinum he carries in his pockets."),
    _(259:  "A lie is a way to tell the truth to someone who doesn't know."),
    _(260:  "Gambling is like the way to power: The only way to win is to cheat, but don't get caught in the process."),
    _(261:  "A wealthy man can afford everything except a conscience."),
    _(262:  "No lobes, no profit."),
    _(263:  "Never let a female in clothes cloud your sense of profit."),
    _(264:  "It's not the size of your planet, but it's income, that matters."),
    _(265:  "The fear of loss may be your greatest enemy or your best friend - choose wisely."),
    _(266:  "A pair of good ears will ring dry a hundred tongues."),
    _(267:  "Wish not so much to live Long, as to live well."),
    _(268:  "a) When in doubt, lie"
          "b) When in doubt, buy"
          "c) When in doubt, demand more money"
          "d) When in doubt, shoot them, take their money, run and blame someone else."),
    _(269:  "Never purchase anything that has been promised to be valuable or go up in value."),
    _(270:  "It's better to have gambled and lost than to never have gambled at all."),
    _(271:  "There's many witty men whose brains can't line their pockets."),
    _(272:  "The way to a Ferengi's heart is through his wallet."),
    _(273:  "Always count their Latinum before selling anything."),
    _(274:  "There is no profit in love; however, a strong heart is worth a few bars of Latinum on the open market. Keep it on ice."),
    _(275:  "Latinum can't buy happiness, but you can sure have a blast renting it."),
    _(276:  "If at first you don't succeed, try to acquire again."),
    _(277:  "Diamonds may be girl's best friend, but you can only buy the girl with Latinum."),
    _(278:  "It's better to swallow your pride than to lose your profit."),
    _(279:  "Never close a deal too soon after a female strokes your lobes."),
    _(280:  "An empty bag can not stand upright."),
    _(281:  "Blood is thicker than water, but harder to sell."),
    _(282:  "Business is like war; it's important to recognize the winner."),
    _(283:  "Rules are always subject to change."),
    _(284:  "Rules are always subject to interpretation."),
    _(285:  "No good deed ever goes unpunished."),
    _(286:  "When Morn leaves it is all over.")
]

class Rules:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roa(self, ctx):
        """Random Rule of Aquisition"""
        
        rule = choice(rules)
        await ctx.send(":orange_book:Rules of Acquisition # "rule)
