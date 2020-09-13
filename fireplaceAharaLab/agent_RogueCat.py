# agent_RogueCat.py

import random

from hearthstone.enums import CardClass, CardType, Race
from utils import ExceptionPlay, Candidate, executeAction, getCandidates
from agent_Standard import postAction

#from agent_RogueCat import printAllRogueCards
def printAllRogueCards():
	from fireplace import cards
	#cards.db.initialize()
	collection = []
	for card in cards.db.keys():
		cls = cards.db[card]
		if not cls.collectible:
			continue
		if cls.type == CardType.HERO:			# Heroes are collectible...
			continue
		if cls.card_class and cls.card_class not in [CardClass.ROGUE, CardClass.NEUTRAL]:# Play with more possibilities
			continue
		collection.append(cls)
	for card in collection:
		dscrpt = card.description
		if '急襲' in dscrpt:
			print("		elif ID  == '%s':"%(card.id))
			print("			myCondition.append(['rush','', ''])")
			print("			#%s : %s"%(card.name, card.description.replace('\n','')))
	return collection

def RogueCatAI(game, option=[], debugLog=False):
	while True:
		myCandidate = getCandidates(game)
		if len(myCandidate)>0:
			if debugLog:
				print '--------------------------'

			myChoice = random.choice(myCandidate)
			executeAction(thisgame, myChoice, debugLog=debugLog)
			postAction(player)
		else:
			return

def haveDragon(game):
	return False


def RogueCat_Condition(game, card, target):
	myCondition=[]#満たしている条件
	cond2=[]#効果
	dscrpt = card.description.replace('\n','')
	player = game.current_player
	myHeroHealth=player.hero.health
	hisHeroHealth=player.opponent.hero.health
	myTauntH = 0
	myMinionH = 0
	myAttack = 0
	for card in player.characters:
		if card.can_attack():
			myAttack += card.atk
		if card.taunt:
			myTauntH += card.health
		if card.type == CardType.MINION:
			myMinionH += card.health
	hisTauntH = 0
	hisAttack = 0
	for card in player.opponent.characters:
		if card.can_attack():
			hisAttack += card.atk
		if card. taunt:
			hisTauntH += card.ahealth
	myHeroRemainder=myHeroHealth+myTaunt-hisAttack
	hisHeroRemainder=hisHeroHealth+hisTaunt-myAttack
	myMinionRemainder=myMinionHealth
	ID = card.id
	if '激励' in dscrpt:#ヒーローパワーを使うと発動する
		#基本的にいつでもあとまわし。内容によっては場との関連がありうる。
		pass
	if  card.charge:#
		if ID == 'AT_070':
			myCondition.append(['charge', 'myRemainder<hisRemainder', 'lessConst'])
		elif ID in {'AT_125', 'UNG_099'}:
			myCondition.append(['charge', 'myRemainder<hisRemainder', 'noAttack'])
		elif ID in {'EX1_116'}:
			myCondition.append(['charge', 'myRemainder<hisRemainder', 'summon'])
		elif ID in {'CS2_146'}:
			if player.hero.weapon != None:
				myCondition.append(['charge', 'myRemainder<hisRemainder', None])
		elif ID in {'CS2_124', 'AT_087', 'CS2_131', 'CS2_171', 'CS2_213', 'EX1_062', 'EX1_067', 'GVG_098'}:
			myCondition.append(['charge', 'myRemainder<hisRemainder', None])
		pass
	if card.has_deathrattle:#断末魔
		myCondition.extend( RogueCat_condition_deathrattle(game))
	if card.has_battlecry:#雄叫び
		myCondition.extend(RogueCat_condition_battlecry(game))
	if '秘策:' in dscrpt:
		myCondition.extend(RogueCat_condition_secret(game))
	if '<b>挑発</b>' in dscrpt:
		myCondition.extend(RogueCat_condition_taunt(game))
	if '聖なる盾' in dscrpt:#一回の攻撃を受けない
		myCondition.extend(RogueCat_condition_devineShield(game))
	if '隠れ身' in dscrpt:#こちらから攻撃するまでの攻撃対象にならない
		myCondition.extend(RogueCat_condition_stealth(game))
	if '呪文ダメージ' in dscrpt:
		myCondition.extend(RogueCat_condition_spellDamage(game))
	if '<b>猛毒</b>' in dscrpt:
		myCondition.extend(RogueCat_condition_poisonous(game))
		pass
	if '<b>超電磁</b>' in dscrpt:
		#<b>超電磁</b>
		pass
	if '<b>急襲</b>' in dscrpt:
		#<b>急襲</b>
		myCondition.extend(RogueCat_condition_rush(game))
	if '<b>生命奪取</b>' in dscrpt:
		#<b>生命奪取</b>
		myCondition.append(['lifeSteal','',''])
		pass
	if '<b>休眠状態</b>' in dscrpt:
		#<b>休眠状態</b>
		myCondition.append(['asleep','',''])
		pass
	if '<b>発見</b>' in dscrpt:
		#<b>発見</b>
		myCondition.append(['discover','',''])
		pass
	if '魔法活性' in dscrpt:#Spellburst
		myCondition.append(['spellBurst','',''])
		pass
########### 度 #################

	if ID=='CFM_325':
		if haveWeapon(game):
			myCondition.append(['weapon','','help'])
			#[CFM_325][ちんけなバッカニーア]([x]自分のヒーローが武器を装備している場合攻撃力+2を得る。)
	elif ID=='NEW1_027':
		if havePirate(game):
			myCondition.append(['pirate','','help'])
			#[NEW1_027][南海の船長](自身を除く味方の海賊は+1/+1を得る。)
	elif ID=='TRL_127':
		if havePirate(game):
			myCondition.append(['pirate','','damage'])
		#[TRL_127][大砲連射]([x]ランダムな敵1体に$3ダメージを与える。味方の海賊1体につき1回これを繰り返す。)




############### コンボ #####################	
	if 'コンボ' in dscrpt:
		if player.combo:
			myCondition.append(['combo','',''])
#[AT_028][シャドーパン騎兵](<b>コンボ:</b> 攻撃力+3を獲得する。)
#[AT_030][アンダーシティの勇士](<b>コンボ:</b> 1ダメージを与える。)
#[BOT_576][イカレた化学者]([x]<b>コンボ:</b>味方のミニオン1体に__攻撃力+4を付与する。)
#[CFM_690][翡翠の手裏剣]([x]__$2ダメージを与える。<b>コンボ:</b> {0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]__$2ダメージを与える。<b>コンボ:</b><b>翡翠のゴーレム</b>を1体召喚する。)
#[CFM_693][ガジェッツァンの渡し守]([x]<b>コンボ:</b>味方のミニオン1体を___自分の手札に戻す。)
#[CS2_073][冷血]([x]ミニオン1体に攻撃力+2を付与する。<b>コンボ:</b> 代わりに攻撃力+4を付与する。)
#[DAL_415][悪党同盟の悪漢]([x]<b>コンボ:</b>ランダムな<b>悪の手先</b>2体を自分の手札に追加する。)
#[DRG_031][ネクリウムの薬師]([x]<b>コンボ:</b>自分のデッキから<b>断末魔</b>を持つミニオンを1体引きその<b>断末魔</b>を獲得する。)
#[EX1_124][腹裂き]([x]$2ダメージを与える。<b>コンボ:</b> 代わりに$4ダメージを与える。)
#[EX1_131][デファイアスの親方]([x]<b>コンボ:</b>2/1のデファイアスの盗賊を1体召喚する。)
#[EX1_133][地獄送りの刃]([x]<b>雄叫び:</b>_____1ダメージを与える。__ <b>コンボ:</b> 代わりに________2ダメージを与える。)
#[EX1_134][SI:7諜報員]([x]<b>コンボ:</b> 2ダメージを与える。)
#[EX1_137][脳天直撃]([x]敵のヒーローに$2ダメージを与える。<b>コンボ:</b> 次のターン、このカードを自分の手札に戻す。)
#[EX1_613][エドウィン・ヴァンクリーフ](<b>コンボ:</b>このターン中で先に使用されたカード1枚につき+2/+2を獲得する。)
#[GIL_557][呪われた漂流者]([x]<b>急襲</b>、<b>断末魔:</b>自分のデッキから<b>コンボ</b>カードを_1枚引く。)
#[GIL_902][人斬りバッカニーア](<b>コンボ:</b>自分の武器に攻撃力+1を__付与する。)
#[GVG_022][ティンカーの刃研ぎ油](自分の武器に攻撃力+3を付与する。<b>コンボ:</b> ランダムな味方のミニオン1体に攻撃力+3を付与する。)
#[GVG_047][サボタージュ]([x]ランダムな敵のミニオン1体を破壊する。<b>コンボ:</b> さらに敵の武器を破壊する。)
#[ICC_809][疫病科学者]([x]<b>コンボ:</b>味方のミニオン1体に<b>猛毒</b>を付与する。)
#[ICC_910][略奪の亡霊]([x]<b>コンボ:</b>このターン中で先に使用したカードの枚数に等しいダメージを与える。)
#[LOOT_211][エルフの吟遊楽人]([x]<b>コンボ:</b>自分のデッキから__ミニオンを2体引く。)
#[NEW1_005][誘拐魔]([x]<b>コンボ:</b> ミニオン1体を___所有者の手札に戻す。)
#[OG_070][凶刃の狂信者]([x]<b>コンボ:</b>______+1/+1を獲得する。)
#[SCH_234][偽善系の二年生]([x]<b>隠れ身</b>、<b>魔法活性:</b><b>コンボ</b>カード1枚を___自分の手札に追加する。)
#[SCH_350][ワンド泥棒]([x]<b>コンボ:</b>メイジの呪文を1つ<b>発見</b>する。)
#[SCH_509][頭を冷やせ！]([x]ミニオン1体を<b>凍結</b>させる。<b>コンボ:</b>さらに$3ダメージを与える。)
#[SCH_521][無理強い]([x]ダメージを受けているミニオン1体を破壊する。<b>コンボ:</b>ミニオン1体を破壊する。)
#[TRL_092][サメの精霊]([x]1ターンの間、<b>隠れ身</b>。味方のミニオンの<b>雄叫び</b>と<b>コンボ</b>は2回発動する。)
#[TRL_124][ぶんどり部隊](自分のデッキから海賊を2体引く。<b>コンボ:</b>さらに武器を1つ引く。)
#[ULD_231][旋風脚流の達人]([x]自分が<b>コンボ</b>カードを手札から使用する度ランダムな<b>コンボ</b>カード1枚を自分の手札に追加する。)
#[ULD_285][鉤付きシミター](<b>コンボ:</b>攻撃力+2を獲得する。)
#[UNG_063][カミツキソウ](<b>コンボ:</b> このターン中で先に使用されたカード1枚につき+1/+1を獲得する。)
#[UNG_064][ヴァイルスパイン・スレイヤー](<b>コンボ:</b>ミニオン1体を破壊する。)
#[YOD_017][影の彫刻家]([x]<b>コンボ:</b>このターン中に先に使用されたカード1枚につきカードを1枚引く。)

#使わない
#[BOT_447][結晶術師]([x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。_____装甲を5獲得する。_)
#[TRL_546][凶暴なリクガメ]([x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。)
#[UNG_087][ビタータイド・ヒドラ](このミニオンがダメージを受ける度自分のヒーローに___3ダメージを与える。)

#自分のヒーローがダメージを受ける度
#ヒーローを攻撃する度
#武器を装備する度

#このミニオンに対して呪文を使用する度
#このミニオンがダメージを受ける度
#このミニオンが攻撃してミニオンを倒す度
#このミニオンが攻撃する度
#味方のミニオンが死ぬ度
#キャラクターが回復を受ける度

#自分が_呪文を使う度
#プレイヤーが呪文を使う度

#相手が呪文を使う度
#自分がカードを引く度
#相手がカードを引く度
#このカードが自分の手札にある間
#<b>雄叫び</b>を持つカードを使う度
#<b>雄叫び</b>を持つミニオンを召喚する度
#自分がカードをデッキに混ぜる度
#<b>秘策</b>が使用される度

#自分がマーロックを召喚する度
#ミニオンを召喚する度
#カードを手札から使用する度
#自分がミニオンを引く度
#カードを手札から使用__する度
#相手がカードを使う度
#自分が海賊を召喚する度
#ミニオンを場に出す度
#味方のメカが死ぬ度
#敵のミニオンが死ぬ度
#自分の武器が破壊される度
#味方のミニオンが死ぬ度

#ミニオンを手札から使用する度
#ミニオンが死ぬ度
#自分が獣を引く度
#手札から呪文が使用される度
#隣接するミニオンがダメージを受ける度
#自分のヒーローの体力を3以上回復する度
#自分が<b>コンボ</b>カードを手札から使用する度
#自分が武器を装備する度

#自分の手札にドラゴンがいる場合
#自分のヒーローの体力を3以上回復する度
#ミニオンが死ぬ度
#自分のデッキに重複するカードがない場合
#自分のターンの終了時
#ダメージを受けている間
#このターンの間
#自分のターンの開始時
#自分が<b>コンボ</b>カードを手札から使用する度
#自分がミニオンを手札から使用する度
#このミニオンを除いて味方に2体以上のミニオンがいる場合





#味方のミニオンが攻撃された時
#自分のターンの終了時
#このターンに自分が呪文を使用した___場合
#味方に体力6以上のミニオンがいる場合
#自分の武器の攻撃力が3以上ある場合
#このミニオンの攻撃でミニオンが 死亡した時
#自分のデッキに重複するカードがない場合
#このターンの間のみ
#相手の陣地に3体以上のミニオンがいる場合
#自分のターンの終了時



def haveBeast(game):
	player = game.current_player
	for card in player.hand:
		if card.race == Race.BEAST:
			return True
	return False

def haveDeathrattle(game):
	player = game.current_player
	for card in player.hand:
		if card.has_deathrattle:
			return True
	return False

def haveDragon(game):
	player = game.current_player
	for card in player.hand:
		if card.race == Race.DRAGON:
			return True
	return False

def haveMinion(game):
	player = game.current_player
	for card in player.field:
		if card.type == CardType.MINION:
			return True
	return False

def havePirate(game):
	player = game.current_player
	for card in player.hand:
		if card.race == Race.PIRATE:
			return True
	return False

def haveWeapon(game):
	player = game.current_player
	for card in player.field:
		if card.type == CardType.WEAPON:
			return True
	return False

def noDeck(game):
	player = game.current_player
	return len(player.deck)==0

def noHand(game):
	player = game.current_player
	return len(player.hand)==0

def noCharacter(game):
   player = game.current_player
   return len(player.characters)==0

def heHasMinion(game):
	player = game.current_player.opponent
	for card in player.field:
		if card.type == CardType.MINION:
			return True
	return False

def heHasDemon(game):
	player = game.current_player.opponent
	for card in player.field:
		if card.race == Race.DEMON:
			return True
	return False

def heHasDeathrattle(game):
	player = game.current_player.opponent
	for card in player.field:
		if card.has_deathrattle:
			return True
	return False

def heHasNonVanilla(game):
	player = game.current_player.opponent
	for card in player.field:
		if len(card.data.descrption)>=3:
			return True
	return False

def heHasTaunt(game):
	player = game.current_player.opponent
	for card in player.field:
		if card.taunt:
			return True
	return False

def haveNoDuplicate(game):
	player = game.current_player
	for card1 in player.field:
		for card2 in player.field:
			if card1!=card2 and card1.name==card2.name:
				return True
	return False

def onPirate(game):
	player = game.current_player
	for card in player.field:
		if card.race == Race.PIRATE:
			return True
	return False
