# agent_RogueCat.py

import random

from hearthstone.enums import CardClass, CardType, Race
from utils import ExceptionPlay, Candidate, executeAction, getCandidates
from agent_Standard import postAction

from agent_RogueCat_1 import *
from agent_RogueCat_2 import *
from agent_RogueCat_3 import *
from agent_RogueCat_4 import *
from agent_RogueCat_5 import *


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
		if 'コンボ' in dscrpt:
			print("		elif ID  == '%s':"%(card.id))
			print("			myCondition.append(['combo','', ''])")
			print("			#%s : %s"%(card.name, card.description.replace('\n','')))
	return collection

def RogueCatAI(game, option=[], debugLog=False):
	while True:
		player = game.current_player
		myCandidate = getCandidates(game)
		if len(myCandidate)>0:
			if debugLog:
				print( '--------------------------')
				for n in range(len(myCandidate)):
					card = myCandidate[n].card
					target = myCandidate[n].target
					myC = RogueCat_Condition(game, card, target)
					print("%r %s : %s"%(card.id, card.data.name, card.data.description.replace('\n','')))
					print("->%r"%target)
					for repeat in range(len(myC)):
						print("%s"%myC[repeat])
				print( '--------------------------')
			myChoice = random.choice(myCandidate)
			executeAction(game, myChoice, debugLog=debugLog)
			postAction(player)
		else:
			return

def haveDragon(game):
	return False



def RogueCat_Condition(game, card, target) -> list:
	myCondition=[]#満たしている条件
	cond2=[]#効果
	dscrpt = card.data.description.replace('\n','')
	player = game.current_player
	myHeroHealth=player.hero.health
	hisHeroHealth=player.opponent.hero.health
	myTauntH = 0
	myMinionH = 0
	myAttack = 0
	for cd in player.characters:
		if cd.can_attack():
			myAttack += cd.atk
		if cd.taunt:
			myTauntH += cd.health
		if cd.type == CardType.MINION:
			myMinionH += cd.health
	hisTauntH = 0
	hisAttack = 0
	for cd in player.opponent.characters:
		if cd.can_attack():
			hisAttack += cd.atk
		if cd. taunt:
			hisTauntH += cd.health
	myHeroRemainder=myHeroHealth+myTauntH-hisAttack
	hisHeroRemainder=hisHeroHealth+hisTauntH-myAttack
	myMinionRemainder=myMinionH
	ID = card.id
	if card.type==CardType.HERO:
		return myCondition
	if '激励' in dscrpt:#ヒーローパワーを使うと発動する
		#基本的にいつでもあとまわし。内容によっては場との関連がありうる。
		pass
	if '突撃' in dscrpt:# card.charge:#突撃
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
	if '断末魔:' in dscrpt:#card.has_deathrattle:#断末魔
		myCondition.extend( RogueCat_condition_deathrattle(game,ID))
	if '雄叫び:' in dscrpt:#card.has_battlecry:#雄叫び
		myCondition.extend(RogueCat_condition_battlecry(game,ID))
	if '秘策:' in dscrpt:
		myCondition.extend(RogueCat_condition_secret(game,ID))
	if '<b>挑発</b>' in dscrpt:
		myCondition.extend(RogueCat_condition_taunt(game,ID))
	if '聖なる盾' in dscrpt:#一回の攻撃を受けない
		myCondition.extend(RogueCat_condition_devineShield(game,ID))
	if '隠れ身' in dscrpt:#こちらから攻撃するまでの攻撃対象にならない
		myCondition.extend(RogueCat_condition_stealth(game,ID))
	if '呪文ダメージ' in dscrpt:
		myCondition.extend(RogueCat_condition_spellDamage(game,ID))
	if '<b>猛毒</b>' in dscrpt:
		myCondition.extend(RogueCat_condition_poisonous(game,ID))
		pass
	if '<b>超電磁</b>' in dscrpt:
		#<b>超電磁</b>
		pass
	if '<b>急襲</b>' in dscrpt:
		#<b>急襲</b>
		myCondition.extend(RogueCat_condition_rush(game,ID))
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
		myCondition.extend(RogueCat_condition_combo(game,ID))

#使わない
#[BOT_447][結晶術師]([x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。_____装甲を5獲得する。_)
#[TRL_546][凶暴なリクガメ]([x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。)
#[UNG_087][ビタータイド・ヒドラ](このミニオンがダメージを受ける度自分のヒーローに___3ダメージを与える。)

#####カード
#自分がカードをデッキに混ぜる度
#自分が<b>コンボ</b>カードを手札から使用する度
#自分がカードを引く度
#相手がカードを引く度
#このカードが自分の手札にある間
#<b>秘策</b>が使用される度
#カードを手札から使用する度
#自分がミニオンを引く度
#カードを手札から使用__する度
#相手がカードを使う度
#自分が獣を引く度
#自分のデッキに重複するカードがない場合
#自分の手札にドラゴンがいる場合
#自分のデッキに重複するカードがない場合
#自分が<b>コンボ</b>カードを手札から使用する度
#自分がミニオンを手札から使用する度

#####召喚
	myCondition.extend(RogueCat_condition_playCard(game,ID))

#####体力など
#自分のヒーローの体力を3以上回復する度
#キャラクターが回復を受ける度
#自分のヒーローがダメージを受ける度
#このミニオンがダメージを受ける度
#隣接するミニオンがダメージを受ける度
#自分のヒーローの体力を3以上回復する度
#ダメージを受けている間

#####装備
#自分が武器を装備する度
	if '武器' in dscrpt:
		if ID  == 'AT_029':
			myCondition.append(['weapon','', ''])
			#バッカニーア : 自分が武器を装備する度、その武器に攻撃力+1を付与する。
		elif ID  == 'AT_034':
			myCondition.append(['weapon','', ''])
			#毒仕込みの刃 : 自分のヒーローパワーはこの武器と置き換わる代わりに、この武器に攻撃力+1を付与する。
		elif ID  == 'CFM_325':
			myCondition.append(['weapon','', ''])
			#ちんけなバッカニーア : [x]自分のヒーローが武器を装備している場合攻撃力+2を得る。
		elif ID  == 'CS2_074':
			myCondition.append(['weapon','', ''])
			#致死毒 : 自分の武器に攻撃力+2を付与する。
		elif ID  == 'CS2_233':
			myCondition.append(['weapon','', ''])
			#千刃乱舞 : 自分の武器を破壊しその攻撃力に等しいダメージを敵のミニオン全てに与える。
		elif ID  == 'GVG_022':
			myCondition.append(['weapon','', ''])
			#ティンカーの刃研ぎ油 : 自分の武器に攻撃力+3を付与する。<b>コンボ:</b> ランダムな味方のミニオン1体に攻撃力+3を付与する。
		elif ID  == 'SCH_519':
			myCondition.append(['weapon','', ''])
			#ヴァルペラの毒刃研究者 : 自分の武器は攻撃力+2を得る。
		elif ID  == 'SCH_623':
			myCondition.append(['weapon','', ''])
			#斧刀講 : [x]カードを2枚引く。自分の武器の攻撃力1につきコストが（1）減る。


#####攻撃
#ヒーローを攻撃する度
#このミニオンが攻撃してミニオンを倒す度
#このミニオンが攻撃する度
#味方のミニオンが攻撃された時

#####呪文
	if '呪文' in dscrpt:
		if ID  == 'AT_129':
			myCondition.append(['spell','', ''])
			#フィヨラ・ライトベイン : <b>自分</b>がこのミニオンに対して呪文を使用する度<b>聖なる盾</b>を獲得する。
		elif ID  == 'AT_131':
			myCondition.append(['spell','', ''])
			#エイディス・ダークベイン : [x]<b>自分</b>がこのミニオンに対して呪文を使用する度ランダムな敵に_____3ダメージを与える。
		elif ID  == 'BOT_098':
			myCondition.append(['spell','', ''])
			#パワー切れのモーラー : [x]このターンに自分が呪文を使用した___場合のみ攻撃できる。
		elif ID  == 'BRM_020':
			myCondition.append(['spell','', ''])
			#ドラゴンキン・ソーサラー : [x]<b>自分</b>がこのミニオンに対して呪文を使用する度+1/+1を獲得する。
		elif ID  == 'BT_709':
			myCondition.append(['spell','', ''])
			#汚い手 : [x]<b>秘策:</b>相手が呪文を使用した後カードを2枚引く。
		elif ID  == 'CFM_060':
			myCondition.append(['spell','', ''])
			#レッド・マナ・ワーム : [x]自分が呪文を使う度攻撃力+2を獲得する。
		elif ID  == 'CFM_669':
			myCondition.append(['spell','', ''])
			#強盗ログ : [x]相手が呪文を使う度自分の手札に「コイン」1枚を追加する。
		elif ID  == 'CFM_807':
			myCondition.append(['spell','', ''])
			#競売王ビアードオ : [x]自分が呪文を使用した後自分のヒーローパワーを再度使用可能にする。
		elif ID  == 'DAL_774':
			myCondition.append(['spell','', ''])
			#異境の乗騎売り : [x]自分が呪文を使う度ランダムなコスト3の__獣1体を召喚する。
		elif ID  == 'EX1_055':
			myCondition.append(['spell','', ''])
			#マナ中毒者 : [x]自分が呪文を使う度そのターンの間攻撃力+2を獲得する。
		elif ID  == 'EX1_095':
			myCondition.append(['spell','', ''])
			#ガジェッツァンの競売人 : 自分が呪文を使う度カードを1枚引く。
		elif ID  == 'EX1_100':
			myCondition.append(['spell','', ''])
			#探話士チョー : プレイヤーが呪文を使う度、もう1人のプレイヤーの手札にその呪文のコピーを追加する。
		elif ID  == 'EX1_187':
			myCondition.append(['spell','', ''])
			#魔力喰らい : [x]自分が呪文を使う度+2/+2を獲得する。
		elif ID  == 'GVG_028':
			myCondition.append(['spell','', ''])
			#商大公ガリーウィックス : [x]相手が呪文を使う度自分はその呪文のコピー1枚を獲得し、相手は「ガリーウィックスの______コイン」1枚を獲得する。_
		elif ID  == 'GVG_067':
			myCondition.append(['spell','', ''])
			#ストーンスプリンター・トログ : [x]相手が呪文を使う度攻撃力+1を獲得する。
		elif ID  == 'GVG_068':
			myCondition.append(['spell','', ''])
			#バーリー・ロックジョー・トログ : [x]相手が呪文を使う度攻撃力+2を獲得する。
		elif ID  == 'GVG_118':
			myCondition.append(['spell','', ''])
			#アーシネイター・トログザー : 相手が呪文を使う度バーリー・ロックジョー・トログを1体召喚する。
		elif ID  == 'ICC_201':
			myCondition.append(['spell','', ''])
			#骰は投げられた : [x]カードを1枚引く。そのカードが<b>断末魔</b>を持つ場合、再度この呪文を使用する。
		elif ID  == 'KAR_036':
			myCondition.append(['spell','', ''])
			#魔力異常体 : [x]自分が呪文を使う度このミニオンに体力+1を付与する。
		elif ID  == 'LOE_053':
			myCondition.append(['spell','', ''])
			#西風のジニー : [x]自分がこのミニオンを除く、味方のミニオンに呪文を使用した後、その呪文をコピーし、このミニオンに対して使用する。
		elif ID  == 'LOE_086':
			myCondition.append(['spell','', ''])
			#召喚石 : 自分が呪文を使う度同コストのランダムなミニオン1体を召喚する。
		elif ID  == 'LOOT_130':
			myCondition.append(['spell','', ''])
			#魔力の暴帝 : [x]このターンにコスト（5）以上の呪文を使用していた場合コスト（0）。
		elif ID  == 'NEW1_020':
			myCondition.append(['spell','', ''])
			#熱狂する火霊術師 : [x]自分が呪文を使用した後全てのミニオンに1ダメージを与える。
		elif ID  == 'NEW1_026':
			myCondition.append(['spell','', ''])
			#ヴァイオレット・アイの講師 : [x]自分が呪文を使う度1/1のヴァイオレット・アイの徒弟を1体召喚する。
		elif ID  == 'SCH_157':
			myCondition.append(['spell','', ''])
			#魔法の大釜 : [x]<b>魔法活性:</b>使われた呪文と同コストのランダムな呪文を使用する。
		elif ID  == 'SCH_710':
			myCondition.append(['spell','', ''])
			#往餓術師 : [x]相手が呪文を使う度<b>挑発</b>を持つ2/2のスケルトンを1体召喚する。
		elif ID  == 'SCH_714':
			myCondition.append(['spell','', ''])
			#英才エレク : [x]手札から呪文が使用される度このミニオンはそれを記憶する。<b>断末魔:</b>_記憶した呪文全てを___自分のデッキに混ぜる。
		elif ID  == 'UNG_843':
			myCondition.append(['spell','', ''])
			#ヴォラックス : 自分がこのミニオンに呪文を使用した後1/1の植物を1体召喚し呪文のコピーをその植物に対して使用する。

#####死去
	if '死' in dscrpt:
		if ID  == 'CFM_658':
			myCondition.append(['death','', ''])
			#奥部屋の用心棒 : [x]味方のミニオンが死ぬ度、攻撃力+1を獲得する。
		elif ID  == 'GIL_819':
			myCondition.append(['death','onMinion(game)', 'drawCard'])
			#魔女の大釜: [x]味方のミニオンが死亡したのち、ランダムなシャーマンの呪文1枚を______自分の手札に追加する。
		elif ID  == 'GVG_106':
			myCondition.append(['death','', ''])
			#ジャンクロボ : [x]味方のメカが死ぬ度+2/+2を獲得する。
		elif ID  == 'GVG_116':
			myCondition.append(['death','', ''])
			#メカジニア・サーマプラッグ : 敵のミニオンが死ぬ度に、レプラノームを1体召喚する。
		elif ID  == 'ICC_900':
			myCondition.append(['death','', ''])
			#壊死のガイスト : [x]このミニオンを除く味方のミニオンが死ぬ度、2/2のグールを1体召喚する。
		elif ID  == 'LOOT_149':
			myCondition.append(['death','', ''])
			#回廊漁り蟲 : [x]このカードが手札にある間ミニオンが死ぬ度コストが（1）減る。
		elif ID  == 'tt_004':
			myCondition.append(['death','', ''])
			#屍肉喰いのグール : [x]ミニオンが死ぬ度攻撃力+1を獲得する。

#####ターン
#自分のターンの終了時
#自分のターンの終了時
#このターンの間のみ
#自分のターンの終了時
#このターンの間
#自分のターンの開始時







	return myCondition


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

def haveMechanical(game):
	player = game.current_player
	for card in player.hand:
		if card.race == Race.MECHANICAL:
			return True
	return False

def haveMinion(game):
	player = game.current_player
	for card in player.hand:
		if card.type == CardType.MINION:
			return True
	return False

def havePirate(game):
	player = game.current_player
	for card in player.hand:
		if card.race == Race.PIRATE:
			return True
	return False

def haveSecret(game):
	player = game.current_player
	if len(player.secrets)>0:
		return True
	return False

def haveWeapon(game):
	return onWeapon(game)

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

def heHasWeapon(game):
	player = game.current_player.opponent
	for card in player.characters:
		if card.type == CardType.WEAPON:
			return True
	return False


def haveNoDuplicate(game):
	player = game.current_player
	for card1 in player.field:
		for card2 in player.field:
			if card1!=card2 and card1.name==card2.name:
				return True
	return False

def OnMechanical(game):
	player = game.current_player
	for card in player.field:
		if card.race == Race.MECHANICAL:
			return True
	return False

def onMinion(game):
	player = game.current_player
	for card in player.field:
		if card.type == CardType.MINION:
			return True
	return False

def onPirate(game):
	player = game.current_player
	for card in player.field:
		if card.race == Race.PIRATE:
			return True
	return False

def onWeapon(game):
	player = game.current_player
	for card in player.characters:
		if card.type == CardType.WEAPON:
			return True
	return False
