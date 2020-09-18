def RogueCat_condition_devineShield(game,ID):
	myCondition=[]
	if ID == 'AT_087':
		myCondition.append(['divineShield','', ''])
		#アージェントの騎兵 : <b>突撃:</b><b>聖なる盾</b>
	elif ID == 'AT_095':
		myCondition.append(['divineShield','', ''])
		#静寂の騎士 : <b>隠れ身</b><b>聖なる盾</b>
	elif ID == 'BOT_414':
		myCondition.append(['divineShield','', ''])
		#クロークスケイルの化学者 : <b>隠れ身</b><b>聖なる盾</b>
	elif ID == 'BOT_534':
		myCondition.append(['divineShield','', ''])
		#ブル・ドーザー : <b>聖なる盾</b>
	elif ID == 'BOT_548':
		myCondition.append(['divineShield','', ''])
		#ジリアックス : <b>超電磁</b><b>聖なる盾</b>、<b>挑発</b><b>生命奪取</b>、<b>急襲</b>
	elif ID == 'DAL_078':
		myCondition.append(['divineShield','', ''])
		#旅の治療師 : <b>聖なる盾</b>、<b>雄叫び:</b>体力を#3回復する。
	elif ID == 'DAL_085':
		myCondition.append(['divineShield','', ''])
		#ダララン・クルセイダー : <b>聖なる盾</b>
	elif ID == 'DRG_079':
		myCondition.append(['divineShield','', ''])
		#躱し身のワーム : <b>聖なる盾</b>、<b>急襲</b>呪文とヒーローパワーの標的にならない。
	elif ID == 'EX1_008':
		myCondition.append(['divineShield','', ''])
		#アージェントの従騎士 : <b>聖なる盾</b>
	elif ID == 'EX1_020':
		myCondition.append(['divineShield','', ''])
		#スカーレット・クルセイダー : <b>聖なる盾</b>
	elif ID == 'EX1_023':
		myCondition.append(['divineShield','', ''])
		#シルバームーンの守護兵 : <b>聖なる盾</b>
	elif ID == 'EX1_032':
		myCondition.append(['divineShield','', ''])
		#サンウォーカー : [x]<b>挑発</b>、<b>聖なる盾</b>
	elif ID == 'EX1_067':
		myCondition.append(['divineShield','', ''])
		#アージェントの司令官 : [x]<b>突撃</b>、<b>聖なる盾</b>
	elif ID == 'GIL_202':
		myCondition.append(['divineShield','', ''])
		#ギルニーアスの近衛兵 : [x]<b>聖なる盾</b>、<b>急襲</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。
	elif ID == 'GVG_079':
		myCondition.append(['divineShield','', ''])
		#フォース・タンクMAX : <b>聖なる盾</b>
	elif ID == 'GVG_085':
		myCondition.append(['divineShield','', ''])
		#マジウザ・オ・トロン : <b>挑発</b><b>聖なる盾</b>
	elif ID == 'ICC_913':
		myCondition.append(['divineShield','', ''])
		#穢れし狂信者 : <b>聖なる盾</b><b>呪文ダメージ+1</b>
	elif ID == 'LOOT_117':
		myCondition.append(['divineShield','', ''])
		#蝋のエレメンタル : <b>挑発</b><b>聖なる盾</b>
	elif ID == 'LOOT_125':
		myCondition.append(['divineShield','', ''])
		#石肌のバジリスク : <b>聖なる盾</b><b>猛毒</b>
	elif ID == 'OG_145':
		myCondition.append(['divineShield','', ''])
		#マジヤバ・オ・トロン : <b>挑発</b>、<b>聖なる盾</b>
	elif ID == 'OG_283':
		myCondition.append(['divineShield','', ''])
		#クトゥーンに選ばれし者 : [x]<b>聖なる盾</b>、<b>雄叫び:</b>自分のクトゥーンに+2/+2を付与する____<i>（居場所は問わない）。</i>
	elif ID == 'SCH_143':
		myCondition.append(['divineShield','', ''])
		#聖レイジャー : <b>聖なる盾</b>
	elif ID == 'TRL_513':
		myCondition.append(['divineShield','', ''])
		#モッシュオグの審判 : <b>挑発</b>、<b>聖なる盾</b>
	elif ID == 'ULD_721':
		myCondition.append(['divineShield','', ''])
		#月の巨像 : <b>聖なる盾</b>、<b>蘇り</b>
	return myCondition

def RogueCat_condition_stealth(game,ID):
	myCondition=[]
	if ID == 'AT_095':
		myCondition.append(['stealth','', ''])
		#静寂の騎士 : <b>隠れ身</b><b>聖なる盾</b>
	elif ID == 'BOT_414':
		myCondition.append(['stealth','', ''])
		#クロークスケイルの化学者 : <b>隠れ身</b><b>聖なる盾</b>
	elif ID == 'BOT_555':
		myCondition.append(['stealth','', ''])
		#先遣者セレスティア : [x]<b>隠れ身</b>相手がミニオンを手札から使用した後そのミニオンの_コピーになる。
	elif ID == 'BT_701':
		myCondition.append(['stealth','', ''])
		#スパイミストレス : <b>隠れ身</b>
	elif ID == 'BT_713':
		myCondition.append(['stealth','', ''])
		#アカマ : [x]<b>隠れ身</b>、<b>断末魔:</b>「転生アカマ」を自分のデッキに混ぜる。
	elif ID == 'CFM_344':
		myCondition.append(['stealth','', ''])
		#飛刀手流忍者・六丸 : [x]<b>隠れ身</b>このミニオンの攻撃でミニオンが 死亡した時、自分のデッキからマーロックを2体召喚する。
	elif ID == 'CFM_634':
		myCondition.append(['stealth','', ''])
		#蓮華凶手 : [x]<b>隠れ身</b>このミニオンが攻撃してミニオンを倒す度に　<b>隠れ身</b>を獲得する。
	elif ID == 'CFM_636':
		myCondition.append(['stealth','', ''])
		#シャドウ・レイジャー : <b>隠れ身</b>
	elif ID == 'CFM_691':
		myCondition.append(['stealth','', ''])
		#翡翠の鎌刀 : [x]<b>隠れ身</b>、 <b>断末魔:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>隠れ身</b>、 <b>断末魔:</b><b>翡翠のゴーレム</b>を1体召喚する。
	elif ID == 'CFM_781':
		myCondition.append(['stealth','', ''])
		#蒐集家シャク : [x]<b>隠れ身</b>このミニオンが攻撃する度相手のクラスのランダムなカード1枚を自分の手札に追加する。
	elif ID == 'CS2_161':
		myCondition.append(['stealth','', ''])
		#レイヴンホルトの暗殺者 : <b>隠れ身</b>
	elif ID == 'DAL_090':
		myCondition.append(['stealth','', ''])
		#ヘンチ・クランの隠密 : <b>隠れ身</b>
	elif ID == 'EX1_010':
		myCondition.append(['stealth','', ''])
		#ウォーゲンのスパイ : <b>隠れ身</b>
	elif ID == 'EX1_017':
		myCondition.append(['stealth','', ''])
		#ジャングル・パンサー : <b>隠れ身</b>
	elif ID == 'EX1_028':
		myCondition.append(['stealth','', ''])
		#ストラングルソーントラ : <b>隠れ身</b>
	elif ID == 'EX1_128':
		myCondition.append(['stealth','', ''])
		#隠蔽 : [x]次の自分のターンまで味方のミニオン全てに<b>隠れ身</b>を付与する。
	elif ID == 'EX1_522':
		myCondition.append(['stealth','', ''])
		#埋伏の暗殺者 : [x]<b>隠れ身</b>、<b>猛毒</b>
	elif ID == 'FP1_005':
		myCondition.append(['stealth','', ''])
		#ナクスラーマスの亡霊 : <b>隠れ身:</b> 自分のターンの開始時+1/+1を獲得する。
#	elif ID == 'GVG_025':
#		myCondition.append(['stealth','', ''])
#		#隻眼のチート : [x]自分が海賊を召喚する度、<b>隠れ身</b>を獲得する。
	elif ID == 'GVG_081':
		myCondition.append(['stealth','', ''])
		#ギルブリン・ストーカー : <b>隠れ身</b>
	elif ID == 'GVG_088':
		myCondition.append(['stealth','', ''])
		#オーガ・ニンジャ : <b>隠れ身:</b>50%の確率で、指定していない敵を攻撃する。
	elif ID == 'GVG_109':
		myCondition.append(['stealth','', ''])
		#ミニ・メイジ : [x]<b>呪文ダメージ+1</b><b>隠れ身</b>
	elif ID == 'KAR_044':
		myCondition.append(['stealth','', ''])
		#モローズ : [x]<b>隠れ身</b>自分のターンの終了時1/1の家令を1体召喚する。
	elif ID == 'LOOT_136':
		myCondition.append(['stealth','', ''])
		#潜む悪鬼 : <b>隠れ身</b>自身を除く味方のミニオンは攻撃力+1を得る。
	elif ID == 'OG_247':
		myCondition.append(['stealth','', ''])
		#ウォーゲン変異体 : <b>隠れ身</b>
	elif ID == 'SCH_234':
		myCondition.append(['stealth','', ''])
		#偽善系の二年生 : [x]<b>隠れ身</b>、<b>魔法活性:</b><b>コンボ</b>カード1枚を___自分の手札に追加する。
	elif ID == 'SCH_426':
		myCondition.append(['stealth','', ''])
		#潜入者リリアン : [x]<b>隠れ身</b>、<b>断末魔:</b>ランダムな敵1体を即座に攻撃する4/2の「フォーセイクンのリリアン」を1体召喚する。
	elif ID == 'SCH_708':
		myCondition.append(['stealth','', ''])
		#日陰草の非行生徒 : [x]<b>隠れ身</b>、<b>断末魔:</b><b>隠れ身</b>を持つ3/1の幽霊1体を自分の___手札に追加する。
	elif ID == 'TRL_010':
		myCondition.append(['stealth','', ''])
		#ハーフタイムの清掃員 : [x]<b>隠れ身</b>、<b>血祭:</b>___装甲を3獲得する。
	elif ID == 'TRL_092':
		myCondition.append(['stealth','', ''])
		#サメの精霊 : [x]1ターンの間、<b>隠れ身</b>。味方のミニオンの<b>雄叫び</b>と<b>コンボ</b>は2回発動する。
	elif ID == 'ULD_274':
		myCondition.append(['stealth','', ''])
		#荒れ地の暗殺者 : <b>隠れ身</b>、<b>蘇り</b>
	elif ID == 'UNG_812':
		myCondition.append(['stealth','', ''])
		#サーベルストーカー : <b>隠れ身</b>
	elif ID == 'UNG_814':
		myCondition.append(['stealth','', ''])
		#巨大スズメバチ : [x]<b>隠れ身</b>、<b>猛毒</b>
	elif ID == 'YOD_006':
		myCondition.append(['stealth','', ''])
		#脱走したマナセイバー : [x]<b>隠れ身</b>これが攻撃する度このターンの間のみマナクリスタルを1つ獲得する。
	elif ID == 'YOD_016':
		myCondition.append(['stealth','', ''])
		#飛掠船員 : <b>隠れ身</b>、<b>断末魔:</b>カードを1枚引く。
	return myCondition

def RogueCat_condition_spellDamage(game,ID):
	myCondition=[]
	#攻撃呪文カードを持っていたら+2
	if haveSpellAttack(game):
		myCondition.append(['spellDamage','',''])
	#if ID == 'AT_093':
	#	myCondition.append(['spellDamage','', ''])
	#	#極寒のスノボルト : <b>呪文ダメージ+1</b>
	#elif ID == 'AT_117':
	#	myCondition.append(['spellDamage','', ''])
	#	#司会者 : <b>雄叫び:</b> 味方に<b>呪文ダメージ</b>を持つミニオンがいる場合、+2/+2を獲得する。
	#elif ID == 'BT_008':
	#	myCondition.append(['spellDamage','', ''])
	#	#錆鉄の入門者 : [x]<b>断末魔:</b><b>呪文ダメージ+1</b>を持つ1/1の「インプキャスター」を1体召喚する。
	#elif ID == 'BT_724':
	#	myCondition.append(['spellDamage','', ''])
	#	#イセリアル改造屋 : [x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え<b>呪文ダメージ+1</b>を付与する。
	#elif ID == 'CFM_039':
	#	myCondition.append(['spellDamage','', ''])
	#	#路上のトリックスター : <b>呪文ダメージ+1</b>
	#elif ID == 'CS2_142':
	#	myCondition.append(['spellDamage','', ''])
	#	#コボルトの地霊術師 : <b>呪文ダメージ+1</b>
	#elif ID == 'CS2_155':
	#	myCondition.append(['spellDamage','', ''])
	#	#大魔術師 : <b>呪文ダメージ+1</b>
	#elif ID == 'CS2_197':
	#	myCondition.append(['spellDamage','', ''])
	#	#オーガのメイジ達 : <b>呪文ダメージ+1</b>
	#elif ID == 'DAL_089':
	#	myCondition.append(['spellDamage','', ''])
	#	#呪文書綴じ師 : [x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合____カードを1枚引く。
	#elif ID == 'DAL_096':
	#	myCondition.append(['spellDamage','', ''])
	#	#ヴァイオレット監獄の看守 : <b>挑発</b><b>呪文ダメージ+1</b>
	#elif ID == 'DAL_434':
	#	myCondition.append(['spellDamage','', ''])
	#	#魔力の番人 : [x]自分が<b>呪文ダメージ</b>を持っていない限り攻撃できない。
	#elif ID == 'DAL_548':
	#	myCondition.append(['spellDamage','', ''])
	#	#アゼライト・エレメンタル : [x]自分のターンの開始時<b>呪文ダメージ+2</b>を得る。
	#elif ID == 'DAL_748':
	#	myCondition.append(['spellDamage','', ''])
	#	#マナタンク : <b>呪文ダメージ+1</b>
	#elif ID == 'EX1_012':
	#	myCondition.append(['spellDamage','', ''])
	#	#ブラッドメイジ・サルノス : [x]<b>呪文ダメージ+1</b><b>断末魔:</b>カードを1枚引く。
	#elif ID == 'EX1_284':
	#	myCondition.append(['spellDamage','', ''])
	#	#アジュア・ドレイク : [x]<b>呪文ダメージ+1</b><b>雄叫び:</b>カードを1枚引く。
	#elif ID == 'EX1_563':
	#	myCondition.append(['spellDamage','', ''])
	#	#マリゴス : <b>呪文ダメージ+5</b>
	#elif ID == 'EX1_582':
	#	myCondition.append(['spellDamage','', ''])
	#	#ダラランのメイジ : <b>呪文ダメージ+1</b>
	#elif ID == 'EX1_584':
	#	myCondition.append(['spellDamage','', ''])
	#	#老練のメイジ : [x]<b>雄叫び:</b> 隣接するミニオンに<b>呪文ダメージ+1</b>を付与する。
	#elif ID == 'GIL_121':
	#	myCondition.append(['spellDamage','', ''])
	#	#ダークマイア・ムーンキン : <b>呪文ダメージ+2</b>
	#elif ID == 'GIL_529':
	#	myCondition.append(['spellDamage','', ''])
	#	#スペルシフター : [x]<b>呪文ダメージ+1</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。
	#elif ID == 'GVG_109':
	#	myCondition.append(['spellDamage','', ''])
	#	#ミニ・メイジ : [x]<b>呪文ダメージ+1</b><b>隠れ身</b>
	#elif ID == 'ICC_093':
	#	myCondition.append(['spellDamage','', ''])
	#	#タスカーの漁師 : [x]<b>雄叫び:</b>味方のミニオン1体に<b>呪文ダメージ+1</b>を付与する。
	#elif ID == 'ICC_856':
	#	myCondition.append(['spellDamage','', ''])
	#	#スペルウィーヴァー : <b>呪文ダメージ+2</b>
	#elif ID == 'ICC_913':
	#	myCondition.append(['spellDamage','', ''])
	#	#穢れし狂信者 : <b>聖なる盾</b><b>呪文ダメージ+1</b>
	#elif ID == 'OG_082':
	#	myCondition.append(['spellDamage','', ''])
	#	#コボルトの地霊呪痛死 : <b>呪文ダメージ+2</b>
	#elif ID == 'SCH_245':
	#	myCondition.append(['spellDamage','', ''])
	#	#筆記の執精 : [x]<b>呪文ダメージ+1</b><b>雄叫び:</b>___呪文を1つ<b>発見</b>する。
	#elif ID == 'SCH_270':
	#	myCondition.append(['spellDamage','', ''])
	#	#根源学の予習 : [x]<b>呪文ダメージ</b>を持つミニオンを1体<b>発見</b>する。自分が次に使用する<b>呪文ダメージ</b>を持つミニオンのコストが（1）減る。
	#elif ID == 'SCH_273':
	#	myCondition.append(['spellDamage','', ''])
	#	#ラス・フロストウィスパー : [x]自分のターンの終了時全ての敵に$1ダメージを与える<i>（<b>呪文ダメージ</b>によって__強化される）</i>。
	#elif ID == 'SCH_530':
	#	myCondition.append(['spellDamage','', ''])
	#	#代理鏡師 : [x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合このミニオンのコピーを1体召喚する。
	#elif ID == 'TRL_312':
	#	myCondition.append(['spellDamage','', ''])
	#	#強仙師 : ダメージを受けている間は<b>呪文ダメージ+2</b>を得る。
	return myCondition

def	RogueCat_condition_playCard(game,ID):
	if ('カードを使う' in dscrpt or '召喚する' in dscrpt or '場に出す' in dscrpt or '使用する' in dscrpt or 'ミニオンがいる' in dscrpt):
		if ID  == 'AT_035':
			myCondition.append(['playCard','', 'drawCard'])
			#土蜘蛛 : [x]相手のデッキに「待ち伏せ！」3枚を混ぜる。「待ち伏せ！」が引かれた際自分の陣地に4/4の_____ネルビアンを1体召喚する。
		elif ID  == 'BOT_280':
			myCondition.append(['playCard','', 'summon'])
			#幻像術師 : [x]相手がミニオンを手札から使用した後そのミニオンの1/1のコピーを1体召喚する。
		elif ID  == 'BRM_019':
			myCondition.append(['playCard','', 'summon'])
			#ぐったりガブ呑み亭の常連 : [x]このミニオンがダメージを受けて生き延びた後「ぐったりガブ呑み亭の常連」をもう1体召喚する。
		elif ID  == 'BRM_022':
			myCondition.append(['playCard','', 'summon'])
			#ドラゴンの卵 : このミニオンがダメージを受ける度2/1のチビドラゴン1体を召喚する。
		elif ID  == 'BT_255':
			myCondition.append(['playCard','', 'help'])
			#ケルサス・サンストライダー : [x]毎ターン、自分が使用する呪文のコストは3回目ごとに（0）になる。
		elif ID  == 'CFM_637':
			myCondition.append(['playCard','havePirate(game)', 'summon'])
			#海賊パッチーズ : [x]自分が海賊を手札から使用した後自分のデッキからこの____ミニオンを召喚する。
		elif ID  == 'DAL_550':
			myCondition.append(['playCard','', 'summon'])
			#最下層ウーズ : [x]このミニオンがダメージを受けて生き延びた後このミニオンのコピーを1体召喚する。
		elif ID  == 'DAL_774':
			myCondition.append(['playCard','', 'summon'])
			#異境の乗騎売り : [x]自分が呪文を使う度ランダムなコスト3の__獣1体を召喚する。
		elif ID  == 'DRG_056':
			myCondition.append(['playCard','havePirate(game)', 'summon'])
			#パラシュート・パイレート : [x]自分が海賊を手札から使用した後自分の手札から____このミニオンを召喚する。
		elif ID  == 'EX1_076':
			myCondition.append(['playCard','', ''])
			#ポケットサイズの召喚師 : 毎ターン最初に手札から使用するミニオンのコストが（1）減る。
		elif ID  == 'EX1_145':
			myCondition.append(['playCard','', ''])
			#段取り : [x]このターン自分が次に使用する呪文のコストが（2）減る。
		elif ID  == 'EX1_509':
			myCondition.append(['playCard','summonMurloc(game)', 'help'])
			#マーロックのタイドコーラー : [x]自分がマーロックを召喚する度___攻撃力+1を獲得する。
		elif ID  == 'EX1_614':
			myCondition.append(['playCard','', 'summon'])
			#ザヴィウス : [x]自分がカードを手札から使用した後2/1のサテュロスを1体召喚する。
		elif ID  == 'GIL_620':
			myCondition.append(['playCard','', 'summon'])
			#人形師ドリアン : [x]自分がミニオンを引く度、そのミニオンの1/1のコピーを1体召喚する。
		elif ID  == 'GVG_016':
			myCondition.append(['playCard','', 'destroyDeck'])
			#フェル・リーヴァー : 相手がカードを使う度自分のデッキの上から3枚のカードを捨てる。
		elif ID  == 'GVG_104':
			myCondition.append(['playCard','haveMinion(game)', 'help'])
			#ホブゴブリン : [x]自分が攻撃力1のミニオンを場に出す度そのミニオンに______+2/+2を付与する。
		elif ID  == 'GVG_116':
			myCondition.append(['playCard','heHasMinion(game)', 'summon'])
			#メカジニア・サーマプラッグ : 敵のミニオンが死ぬ度に、レプラノームを1体召喚する。
		elif ID  == 'GVG_118':
			myCondition.append(['playCard','', 'summon'])
			#アーシネイター・トログザー : 相手が呪文を使う度バーリー・ロックジョー・トログを1体召喚する。
		elif ID  == 'ICC_900':
			myCondition.append(['playCard','', 'summon'])
			#壊死のガイスト : [x]このミニオンを除く味方のミニオンが死ぬ度、2/2のグールを1体召喚する。
		elif ID  == 'ICC_911':
			myCondition.append(['playCard','', 'destroyDeck'])
			#号泣のバンシー : [x]自分がカードを使う度自分のデッキの上から3枚のカードを除去する。
		elif ID  == 'LOE_053':
			myCondition.append(['playCard','', ''])
			#西風のジニー : [x]自分がこのミニオンを除く、味方のミニオンに呪文を使用した後、その呪文をコピーし、このミニオンに対して使用する。
		elif ID  == 'LOE_086':
			myCondition.append(['playCard','', 'summon'])
			#召喚石 : 自分が呪文を使う度同コストのランダムなミニオン1体を召喚する。
		elif ID  == 'LOE_107':
			myCondition.append(['playCard','NoMinion(game)', ''])
			#不気味な像 : [x]戦場に他のミニオンがいると攻撃できない。
		elif ID  == 'NEW1_026':
			myCondition.append(['playCard','', 'summon'])
			#ヴァイオレット・アイの講師 : [x]自分が呪文を使う度1/1のヴァイオレット・アイの徒弟を1体召喚する。
		elif ID  == 'TRL_507':
			myCondition.append(['playCard','', 'summon'])
			#シャークフィンのファン : [x]自分のヒーローが攻撃した後1/1の海賊を1体召喚する。
		elif ID  == 'ULD_286':
			myCondition.append(['playCard','haveMinion(game)', 'addCardDeck'])
			#死の影 : [x]ミニオン1体を選択する。引かれた際そのコピー1体を召喚する「影」3枚を自分のデッキに混ぜる。
		elif ID  == 'ULD_290':
			myCondition.append(['playCard','haveMinion(game)', 'help'])
			#歴史愛好家 : [x]自分がミニオンを手札から使用する度自分の手札のランダムなミニオン1体に+1/+1を付与する。
		elif ID  == 'UNG_843':
			myCondition.append(['playCard','haveSpell(game)', 'summon'])
			#ヴォラックス : 自分がこのミニオンに呪文を使用した後1/1の植物を1体召喚し呪文のコピーをその植物に対して使用する。
		pass

def RogueCat_condition_combo(game,ID):
	if player.combo:
		if ID  == 'AT_028':
			myCondition.append(['combo','', 'help'])
			#シャドーパン騎兵 : <b>コンボ:</b> 攻撃力+3を獲得する。
		elif ID  == 'AT_030':
			myCondition.append(['combo','', 'damage'])
			#アンダーシティの勇士 : <b>コンボ:</b> 1ダメージを与える。
		elif ID  == 'BOT_576':
			myCondition.append(['combo','', 'help'])
			#イカレた化学者 : [x]<b>コンボ:</b>味方のミニオン1体に__攻撃力+4を付与する。
		elif ID  == 'CFM_690':
			myCondition.append(['combo','', 'summon'])
			#myCondition.append(['play','', 'damage'])
			#翡翠の手裏剣 : [x]__$2ダメージを与える。<b>コンボ:</b> {0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]__$2ダメージを与える。<b>コンボ:</b><b>翡翠のゴーレム</b>を1体召喚する。
		elif ID  == 'CFM_693':
			myCondition.append(['combo','', 'backCardHand'])
			#ガジェッツァンの渡し守 : [x]<b>コンボ:</b>味方のミニオン1体を___自分の手札に戻す。
		elif ID  == 'CS2_073':
			myCondition.append(['combo','', 'help'])
			#myCondition.append(['play','', 'help'])
			#冷血 : [x]ミニオン1体に攻撃力+2を付与する。<b>コンボ:</b> 代わりに攻撃力+4を付与する。
		elif ID  == 'DAL_415':
			myCondition.append(['combo','', 'drawCard'])
			#悪党同盟の悪漢 : [x]<b>コンボ:</b>ランダムな<b>悪の手先</b>2体を自分の手札に追加する。
		elif ID  == 'DRG_031':
			myCondition.append(['combo','', 'drawCard'])
			#ネクリウムの薬師 : [x]<b>コンボ:</b>自分のデッキから<b>断末魔</b>を持つミニオンを1体引きその<b>断末魔</b>を獲得する。
		elif ID  == 'EX1_124':
			myCondition.append(['playCard','', 'damage'])
			myCondition.append(['combo','', 'damage'])
			#腹裂き : [x]$2ダメージを与える。<b>コンボ:</b> 代わりに$4ダメージを与える。
		elif ID  == 'EX1_131':
			myCondition.append(['combo','', 'summon'])
			#デファイアスの親方 : [x]<b>コンボ:</b>2/1のデファイアスの盗賊を1体召喚する。
		elif ID  == 'EX1_133':
			myCondition.append(['combo','', 'damage'])
			#地獄送りの刃 : [x]<b>雄叫び:</b>_____1ダメージを与える。__ <b>コンボ:</b> 代わりに________2ダメージを与える。
		elif ID  == 'EX1_134':
			myCondition.append(['combo','', 'damage'])
			#SI:7諜報員 : [x]<b>コンボ:</b> 2ダメージを与える。
		elif ID  == 'EX1_137':
			myCondition.append(['playCard','', 'damage'])
			myCondition.append(['combo','', 'backCardHand'])
			#脳天直撃 : [x]敵のヒーローに$2ダメージを与える。<b>コンボ:</b> 次のターン、このカードを自分の手札に戻す。
		elif ID  == 'EX1_613':
			myCondition.append(['combo','', 'help'])
			#エドウィン・ヴァンクリーフ : <b>コンボ:</b>このターン中で先に使用されたカード1枚につき+2/+2を獲得する。
		elif ID  == 'GIL_902':
			myCondition.append(['combo','', 'help'])
			#人斬りバッカニーア : <b>コンボ:</b>自分の武器に攻撃力+1を__付与する。
		elif ID  == 'GVG_022':
			myCondition.append(['combo','', 'help'])
			#ティンカーの刃研ぎ油 : 自分の武器に攻撃力+3を付与する。<b>コンボ:</b> ランダムな味方のミニオン1体に攻撃力+3を付与する。
		elif ID  == 'GVG_047':
			myCondition.append(['combo','heHasWeapon(game)', 'damage'])
			myCondition.append(['combo','heHasMinion(game)', 'damage'])
			#サボタージュ : [x]ランダムな敵のミニオン1体を破壊する。<b>コンボ:</b> さらに敵の武器を破壊する。
		elif ID  == 'ICC_809':
			myCondition.append(['combo','onMinion(game)', 'damageSelf'])
			#疫病科学者 : [x]<b>コンボ:</b>味方のミニオン1体に<b>猛毒</b>を付与する。
		elif ID  == 'ICC_910':
			myCondition.append(['combo','', 'damage'])
			#略奪の亡霊 : [x]<b>コンボ:</b>このターン中で先に使用したカードの枚数に等しいダメージを与える。
		elif ID  == 'LOOT_211':
			myCondition.append(['combo','', 'drawCard'])
			#エルフの吟遊楽人 : [x]<b>コンボ:</b>自分のデッキから__ミニオンを2体引く。
		elif ID  == 'NEW1_005':
			myCondition.append(['combo','', 'backCardHand'])
			#誘拐魔 : [x]<b>コンボ:</b> ミニオン1体を___所有者の手札に戻す。
		elif ID  == 'OG_070':
			myCondition.append(['combo','', 'help'])
			#凶刃の狂信者 : [x]<b>コンボ:</b>______+1/+1を獲得する。
		elif ID  == 'SCH_350':
			myCondition.append(['combo','', 'drawCard'])
			#ワンド泥棒 : [x]<b>コンボ:</b>メイジの呪文を1つ<b>発見</b>する。
		elif ID  == 'SCH_509':
			myCondition.append(['combo','', 'damage'])
			myCondition.append(['playCard','', 'freeze'])
			#頭を冷やせ！ : [x]ミニオン1体を<b>凍結</b>させる。<b>コンボ:</b>さらに$3ダメージを与える。
		elif ID  == 'SCH_521':
			myCondition.append(['playCard','onMinion(game)', 'damageSelf'])
			myCondition.append(['combo','heHasMinion(game)', 'damage'])
			#無理強い : [x]ダメージを受けているミニオン1体を破壊する。<b>コンボ:</b>ミニオン1体を破壊する。
		elif ID  == 'TRL_092':
			myCondition.append(['playCard','', 'help'])
			#サメの精霊 : [x]1ターンの間、<b>隠れ身</b>。味方のミニオンの<b>雄叫び</b>と<b>コンボ</b>は2回発動する。
		elif ID  == 'TRL_124':
			myCondition.append(['playCard','', 'drawCard'])
			myCondition.append(['combo','', 'drawCard'])
			#ぶんどり部隊 : 自分のデッキから海賊を2体引く。<b>コンボ:</b>さらに武器を1つ引く。
		elif ID  == 'ULD_231':
			myCondition.append(['playCard','', 'drawCard'])
			#旋風脚流の達人 : [x]自分が<b>コンボ</b>カードを手札から使用する度ランダムな<b>コンボ</b>カード1枚を自分の手札に追加する。
		elif ID  == 'ULD_285':
			myCondition.append(['combo','', 'help'])
			#鉤付きシミター : <b>コンボ:</b>攻撃力+2を獲得する。
		elif ID  == 'UNG_063':
			myCondition.append(['combo','', 'help'])
			#カミツキソウ : <b>コンボ:</b> このターン中で先に使用されたカード1枚につき+1/+1を獲得する。
		elif ID  == 'UNG_064':
			myCondition.append(['combo','', 'damage'])
			#ヴァイルスパイン・スレイヤー : <b>コンボ:</b>ミニオン1体を破壊する。
		elif ID  == 'YOD_017':
			myCondition.append(['combo','', 'drawCard'])
			#影の彫刻家 : [x]<b>コンボ:</b>このターン中に先に使用されたカード1枚につきカードを1枚引く。
