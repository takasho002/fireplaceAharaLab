def RogueCat_condition_battlecry(game,ID):
	myCondition=[]
	#雄叫び。場に出たときに発動 battlecry
	#基本的にいつでも。内容によっては場との関連がありうる。
	#内容の精査が必要
	if 'AT_' in ID:
		if ID == 'AT_017':
			myCondition.append(['battlecry','haveDragon(game)', ''])
			#トワイライトの守護者 : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合、攻撃力+1と<b>挑発</b>を獲得する。
		elif ID == 'AT_032':
			myCondition.append(['battlecry','havePirate(game) or onPirate(game)', ''])
			#闇商人 : [x]<b>雄叫び:</b>味方に海賊がいる場合___+1/+1を獲得する。
		elif ID == 'AT_084':
			myCondition.append(['battlecry','haveMinion(game)', ''])
			#槍持ち : <b>雄叫び:</b> 味方のミニオン1体に攻撃力+2を付与する。
		elif ID == 'AT_086':
			myCondition.append(['battlecry','', ''])
			#妨害工作員 : [x]<b>雄叫び:</b> 次のターン、相手のヒーローパワーの____コストが（5）増える。
		elif ID == 'AT_094':
			myCondition.append(['battlecry','', ''])
			#火炎ジャグラー : <b>雄叫び:</b>ランダムな敵1体に1ダメージを与える。
		elif ID == 'AT_096':
			myCondition.append(['battlecry','', ''])
			#ゼンマイ仕掛けの騎士 : [x]<b>雄叫び:</b> 味方のメカ1体に__+1/+1を付与する。
		elif ID == 'AT_098':
			myCondition.append(['battlecry','', ''])
			#大道芸の呪文喰い : [x]<b>雄叫び:</b>相手のヒーローパワーをコピーする。
		elif ID == 'AT_103':
			myCondition.append(['battlecry','', ''])
			#北海のクラーケン : <b>雄叫び:</b> 4ダメージを与える。
		elif ID == 'AT_105':
			myCondition.append(['battlecry','', ''])
			#傷を負ったクヴァルディル : <b>雄叫び:</b> このミニオンに3ダメージを与える。
		elif ID == 'AT_106':
			myCondition.append(['battlecry','heHasDemon(game)', 'silence'])
			#光の勇者 : <b>雄叫び:</b> 悪魔1体を<b>沈黙</b>させる。
		elif ID == 'AT_108':
			myCondition.append(['battlecry','', ''])
			#重装戦馬 : [x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、<b>突撃</b>を獲得する。
		elif ID == 'AT_111':
			myCondition.append(['battlecry','', ''])
			#スナック売り : <b>雄叫び:</b>各ヒーローの体力を#4回復する。
		elif ID == 'AT_112':
			myCondition.append(['battlecry','', ''])
			#槍試合の名手 : [x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合、<b>挑発</b>と___<b>聖なる盾</b>を獲得する。
		elif ID == 'AT_115':
			myCondition.append(['battlecry','', ''])
			#フェンシングのコーチ : <b>雄叫び:</b> [x]次に自分のヒーローパワーを使う時、そのコストが（2）減る。
		elif ID == 'AT_117':
			myCondition.append(['battlecry','', ''])
			#司会者 : <b>雄叫び:</b> 味方に<b>呪文ダメージ</b>を持つミニオンがいる場合、+2/+2を獲得する。
		elif ID == 'AT_118':
			myCondition.append(['battlecry','', ''])
			#グランド・クルセイダー : <b>雄叫び:</b> ランダムなパラディン用カード1枚を自分の手札に追加する。
		elif ID == 'AT_122':
			myCondition.append(['battlecry','', ''])
			#串刺しのゴーモック : <b>雄叫び:</b> このミニオンを除いて味方に4体以上ミニオンがいる場合4ダメージを与える。
		elif ID == 'AT_132':
			myCondition.append(['battlecry','', ''])
			#ジャスティサー・トゥルーハート : [x]<b>雄叫び:</b>自分のヒーローパワーが強化版に代わる。
		elif ID == 'AT_133':
			myCondition.append(['battlecry','', ''])
			#ガジェッツァンの槍試合選手 : [x]<b>雄叫び:</b> 各プレイヤーのデッキのミニオンを1枚ずつ表示する。自分のミニオンの方がコストが高い場合__+1/+1を獲得する。
	elif 'BOT_' in ID:
		if ID == 'BOT_079':
			myCondition.append(['battlecry','', ''])
			#忠実ロボ・ルミ : [x]<b>雄叫び:</b>味方のメカ1体に__+1/+1を付与する。
		elif ID == 'BOT_083':
			myCondition.append(['battlecry','', ''])
			#毒物学者 : [x]<b>雄叫び:</b>自分の武器に___攻撃力+1を付与する。
		elif ID == 'BOT_243':
			myCondition.append(['battlecry','', ''])
			#マイラ・ロットスプリング : [x]<b>雄叫び:</b><b>断末魔</b>を持つミニオンを1体<b>発見</b>する。さらにそのミニオンの__<b>断末魔</b>を獲得する。
		elif ID == 'BOT_270':
			myCondition.append(['battlecry','', ''])
			#含み笑う発明家 : [x]<b>雄叫び:</b><b>挑発</b>と<b>聖なる盾</b>を持つ1/2のメカを__2体召喚する。
		elif ID == 'BOT_283':
			myCondition.append(['battlecry','', ''])
			#ホッピング・ホッパー : [x]<b>雄叫び:</b>この対戦で自分が手札から使用した他の「ホッピング・ホッパー」1体につき_+2/+2を獲得する。
		elif ID == 'BOT_288':
			myCondition.append(['battlecry','', ''])
			#ラボの採用担当者 : [x]<b>雄叫び:</b>味方のミニオン1体のコピー3枚を____自分のデッキに混ぜる。
		elif ID == 'BOT_296':
			myCondition.append(['battlecry','', ''])
			#オメガ・ディフェンダー : [x]<b>挑発</b><b>雄叫び:</b> 自分のマナクリスタルが10個ある場合_____攻撃力+10を獲得する。_
		elif ID == 'BOT_308':
			myCondition.append(['battlecry','', ''])
			#スプリング・ロケット : <b>雄叫び:</b>2ダメージを与える。
		elif ID == 'BOT_413':
			myCondition.append(['battlecry','', ''])
			#ブレインストーマー : [x]<b>雄叫び:</b>自分の手札の呪文1枚につき_____体力+1を獲得する。
		elif ID == 'BOT_431':
			myCondition.append(['battlecry','', ''])
			#グルグルグライダー : [x]<b>雄叫び:</b>0/2の「ゴブリン爆弾」を1体召喚する。
		elif ID == 'BOT_447':
			myCondition.append(['battlecry','', ''])
			#結晶術師 : [x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。_____装甲を5獲得する。_
		elif ID == 'BOT_448':
			myCondition.append(['battlecry','', ''])
			#損傷したステゴトロン : <b>挑発</b><b>雄叫び:</b>このミニオンに__6ダメージを与える。
		elif ID == 'BOT_511':
			myCondition.append(['battlecry','', ''])
			#シーフォーリウム・ボンバー : [x]<b>雄叫び:</b>相手のデッキに「爆弾」1枚を混ぜる。「爆弾」は引かれた際に爆発し__5ダメージを与える。
		elif ID == 'BOT_532':
			myCondition.append(['battlecry','', ''])
			#エクスプローディネーター : [x]<b>雄叫び:</b>0/2の「ゴブリン爆弾」を___2体召喚する。
		elif ID == 'BOT_535':
			myCondition.append(['battlecry','', ''])
			#マイクロロボ操縦者 : [x]<b>雄叫び:</b>1/1の「マイクロロボ」を___2体召喚する。
		elif ID == 'BOT_538':
			myCondition.append(['battlecry','', ''])
			#スパーク・エンジン : [x]<b>雄叫び:</b><b>急襲</b>を持つ1/1の「スパーク」1体を____自分の手札に追加する。
		elif ID == 'BOT_539':
			myCondition.append(['battlecry','', ''])
			#魔力ダイナモ : [x]<b>雄叫び:</b>コスト（5）以上の呪文を1枚<b>発見</b>する。
		elif ID == 'BOT_540':
			myCondition.append(['battlecry','', ''])
			#電磁パルス工作員 : [x]<b>雄叫び:</b>__メカ1体を破壊する。
		elif ID == 'BOT_544':
			myCondition.append(['battlecry','', ''])
			#逃走する試験体 : [x]<b>雄叫び:</b>合計6ダメージを自身を除く味方のミニオンにランダムに振り分ける。
		elif ID == 'BOT_550':
			myCondition.append(['battlecry','', ''])
			#電気職工 : [x]<b>雄叫び:</b>自分の手札にコスト（5）以上の呪文がある場合__+1/+1を獲得する。
		elif ID == 'BOT_552':
			myCondition.append(['battlecry','', ''])
			#天体配列者 : [x]<b>雄叫び:</b>味方に体力7のミニオンが3体以上いる場合全ての敵に_7ダメージを与える。
		elif ID == 'BOT_562':
			myCondition.append(['battlecry','', ''])
			#カッパーテイルモドキ : [x]<b>雄叫び:</b>次の自分のターンまで__<b>隠れ身</b>を獲得する。
		elif ID == 'BOT_573':
			myCondition.append(['battlecry','', ''])
			#実験台9号 : <b>雄叫び:</b>自分のデッキから異なる<b>秘策</b>を5枚引く。
		elif ID == 'BOT_907':
			myCondition.append(['battlecry','', ''])
			#電設ロボ : <b>雄叫び:</b>自分の手札のメカ全てのコストを（1）減らす。
	elif 'BRM_' in ID:
		if ID == 'BRM_008':
			myCondition.append(['battlecry','', ''])
			#ダークアイアン・スカルカー : [x]<b>雄叫び:</b>ダメージを受けていない敵のミニオン全てに____2ダメージを与える。
		elif ID == 'BRM_024':
			myCondition.append(['battlecry','', ''])
			#ドラコニッド・クラッシャー : [x]<b>雄叫び:</b> 相手の体力が15以下の場合____+3/+3を獲得する。
		elif ID == 'BRM_026':
			myCondition.append(['battlecry','', ''])
			#腹ペコのドラゴン : <b>雄叫び:</b> ランダムなコスト1のミニオン1体を相手の陣地に召喚する。
		elif ID == 'BRM_029':
			myCondition.append(['battlecry','', ''])
			#レンド・ブラックハンド : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合<b>レジェンド</b>ミニオン1体を破壊する。
		elif ID == 'BRM_030':
			myCondition.append(['battlecry','', ''])
			#ネファリアン : [x]<b>雄叫び:</b><i>相手のクラスの</i>ランダムな呪文2枚を____自分の手札に追加する。
		elif ID == 'BRM_033':
			myCondition.append(['battlecry','', ''])
			#ブラックウィングの技術者 : [x]<b>雄叫び:</b> 自分の手札にドラゴンがいる場合____+1/+1を獲得する。
		elif ID == 'BRM_034':
			myCondition.append(['battlecry','', ''])
			#ブラックウィングの変性者 : [x]<b>雄叫び:</b> 自分の手札にドラゴンがいる場合_____3ダメージを与える。
	elif 'BT_' in ID:
		if ID == 'BT_010':
			myCondition.append(['battlecry','', ''])
			#フェルフィンのナビ : <b>雄叫び:</b>自身を除く味方のマーロックに___+1/+1を付与する。
		elif ID == 'BT_126':
			myCondition.append(['battlecry','', ''])
			#テロン・ゴアフィーンド : [x]<b>雄叫び:</b>自身を除く味方のミニオン全てを破壊する。<b>断末魔:</b>それらに+1/+1を付与し再度召喚する。
		elif ID == 'BT_159':
			myCondition.append(['battlecry','', ''])
			#テラーガードの逃亡者 : <b>雄叫び:</b>相手の陣地に1/1の「追手」を___3体召喚する。
		elif ID == 'BT_160':
			myCondition.append(['battlecry','', ''])
			#錆鉄の狂信者 : [x]<b>雄叫び:</b>自身を除く味方のミニオンに「<b>断末魔</b>:_1/1の悪魔を1体召喚する」を付与する。
		elif ID == 'BT_702':
			myCondition.append(['battlecry','', ''])
			#アッシュタン・スレイヤー : [x]<b>雄叫び:</b><b>隠れ身</b>状態のミニオン1体にこのターンの間、攻撃力+3と<b>無敵</b>を付与する。
		elif ID == 'BT_710':
			myCondition.append(['battlecry','', ''])
			#グレイハート族の賢者 : [x]<b>雄叫び:</b>味方に<b>隠れ身</b>状態のミニオンがいる場合______カードを2枚引く。__
		elif ID == 'BT_711':
			myCondition.append(['battlecry','', ''])
			#脳天直撃ガール : [x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合ミニオン1体を所有者の手札に戻す。そのコストは（1）増える。
		elif ID == 'BT_714':
			myCondition.append(['battlecry','', ''])
			#冷たき影の紡ぎ手 : <b>雄叫び:</b>敵1体を<b>凍結</b>させる。
		elif ID == 'BT_717':
			myCondition.append(['battlecry','', ''])
			#穴掘りスコーピッド : [x]<b>雄叫び:</b>2ダメージを与える。これにより対象が死んだ場合<b>隠れ身</b>を獲得する。
		elif ID == 'BT_720':
			myCondition.append(['battlecry','', ''])
			#錆鉄騎の略奪者 : <b>挑発</b>、<b>急襲</b><b>雄叫び:</b>このターンの間__攻撃力+4を獲得する。
		elif ID == 'BT_722':
			myCondition.append(['battlecry','', ''])
			#ガーディアン改造屋 : [x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え_____<b>聖なる盾</b>を付与する。_
		elif ID == 'BT_723':
			myCondition.append(['battlecry','', ''])
			#ロケット改造屋 : [x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え_____<b>急襲</b>を付与する。_
		elif ID == 'BT_724':
			myCondition.append(['battlecry','', ''])
			#イセリアル改造屋 : [x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え<b>呪文ダメージ+1</b>を付与する。
		elif ID == 'BT_729':
			myCondition.append(['battlecry','', ''])
			#荒野の看守 : [x]<b>雄叫び:</b>ミニオン1体と、同種族の他のミニオン全てに__3ダメージを与える。
		elif ID == 'BT_732':
			myCondition.append(['battlecry','', ''])
			#鋼拾いのシヴァーラ : [x]<b>雄叫び:</b>合計6ダメージを自身を除くミニオンに____ランダムに振り分ける。_
		elif ID == 'BT_737':
			myCondition.append(['battlecry','', ''])
			#マイエヴ・シャドウソング : [x]<b>雄叫び:</b>ミニオン1体を選択する。そのミニオンは2ターンの間<b>休眠状態</b>になる。
		elif ID == 'BT_850':
			myCondition.append(['battlecry','', ''])
			#マグゼリドン : [x]<b>休眠状態</b>。<b>雄叫び:</b>敵の陣地に1/3の結界師を3体召喚する。それらが死んだ時全てのミニオンを破壊して目覚める。
	elif 'CFM_' in ID:
		if ID == 'CFM_063':
			myCondition.append(['battlecry','', ''])
			#妙ちくりんな薬剤師 : [x]<b>雄叫び:</b> ミニオン1体の攻撃力と体力を入れ替える。
		elif ID == 'CFM_067':
			myCondition.append(['battlecry','', ''])
			#ホーゼンの治療師 : [x]<b>雄叫び:</b> ミニオン1体の体力を____上限まで回復する。
		elif ID == 'CFM_321':
			myCondition.append(['battlecry','', ''])
			#グライムストリートの情報屋 : [x]<b>雄叫び:</b>ハンター、パラディンまたはウォリアーの　カードを1枚<b>発見</b>する。
		elif ID == 'CFM_328':
			myCondition.append(['battlecry','', ''])
			#闘技プロモーター : <b>雄叫び:</b> 味方に体力6以上のミニオンがいる場合カードを2枚引く。
		elif ID == 'CFM_342':
			myCondition.append(['battlecry','', ''])
			#幸運のお守りのバッカニーア : [x]<b>雄叫び:</b>自分の武器の攻撃力が3以上ある場合____+4/+4を獲得する。
		elif ID == 'CFM_619':
			myCondition.append(['battlecry','', ''])
			#カバールの薬剤師 : [x]<b>雄叫び:</b>ランダムなポーション1枚を自分の手札に追加する。
		elif ID == 'CFM_621':
			myCondition.append(['battlecry','', ''])
			#カザカス : [x]<b>雄叫び:</b>自分のデッキに重複するカードがない場合_____即興呪文を1つ作成する。
		elif ID == 'CFM_647':
			myCondition.append(['battlecry','', ''])
			#ブロウギル・スナイパー : [x]<b>雄叫び:</b> 1ダメージを与える。
		elif ID == 'CFM_648':
			myCondition.append(['battlecry','', ''])
			#暗黒街の大物 : <b>雄叫び:</b>6/6のオーガを1体召喚する。
		elif ID == 'CFM_649':
			myCondition.append(['battlecry','', ''])
			#カバールの飛脚 : [x]<b>雄叫び:</b>メイジ、プリーストまたはウォーロックの　カードを1枚<b>発見</b>する。
		elif ID == 'CFM_651':
			myCondition.append(['battlecry','', ''])
			#ナーガの海賊 : [x]<b>雄叫び:</b>自分の武器に___攻撃力+1を付与する。
		elif ID == 'CFM_655':
			myCondition.append(['battlecry','', ''])
			#有毒下水ウーズ : [x]<b>雄叫び:</b>敵の武器の耐久度を1減らす。
		elif ID == 'CFM_656':
			myCondition.append(['battlecry','', ''])
			#裏街の探偵 : <b>雄叫び:</b> 敵のミニオンは<b>隠れ身</b>を失う。
		elif ID == 'CFM_659':
			myCondition.append(['battlecry','', ''])
			#ガジェッツァンのセレブ : <b>雄叫び:</b>体力を#2回復する。
		elif ID == 'CFM_667':
			myCondition.append(['battlecry','', ''])
			#爆弾部隊 : [x]<b>雄叫び:</b> 敵のミニオン1体に5ダメージを与える。<b>断末魔:</b> 自分のヒーローに5ダメージを与える。
		elif ID == 'CFM_668':
			myCondition.append(['battlecry','', ''])
			#ドッペルギャングスター : [x]<b>雄叫び:</b>このミニオンのコピーを2体召喚する。
		elif ID == 'CFM_672':
			myCondition.append(['battlecry','', ''])
			#マダム・ゴヤ : [x]<b>雄叫び:</b>味方のミニオン1体を選択する。そのミニオンを自分のデッキのミニオン1体と入れ替える。
		elif ID == 'CFM_685':
			myCondition.append(['battlecry','', ''])
			#ドン・ハン＝チョー : <b>雄叫び:</b>自分の手札のランダムなミニオン1体に+5/+5を付与する。
		elif ID == 'CFM_688':
			myCondition.append(['battlecry','', ''])
			#トゲ付きのホグライダー : [x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオンがいる場合_____<b>突撃</b>を獲得する。
		elif ID == 'CFM_694':
			myCondition.append(['battlecry','', ''])
			#影の師匠 : [x]<b>雄叫び:</b><b>隠れ身</b>を持つミニオン1体に　+2/+2を付与する。
		elif ID == 'CFM_715':
			myCondition.append(['battlecry','', ''])
			#翡翠の精霊 : [x]<b>雄叫び:</b>{0}の<b>翡翠のゴーレム</b>を1体召喚する。@[x]<b>雄叫び:</b><b>翡翠のゴーレム</b>を1体召喚する。
		elif ID == 'CFM_790':
			myCondition.append(['battlecry','', ''])
			#ドブネズミ : [x]<b>挑発</b>、<b>雄叫び:</b>相手は手札からランダムなミニオンを1体召喚する。
		elif ID == 'CFM_806':
			myCondition.append(['battlecry','', ''])
			#ラシオン : [x]<b>挑発</b>、<b>雄叫び:</b>ドラゴン以外のカードを引くまでカードを引く。
		elif ID == 'CFM_809':
			myCondition.append(['battlecry','', ''])
			#タナリスのホグチョッパー : [x]<b>雄叫び:</b>相手が手札を1枚も持っていない場合<b>突撃</b>を獲得する。
		elif ID == 'CFM_810':
			myCondition.append(['battlecry','', ''])
			#ピチピチレザーのホグリーダー : [x]<b>雄叫び:</b>相手の手札が6枚以上ある場合_____<b>突撃</b>を獲得する。
		elif ID == 'CFM_852':
			myCondition.append(['battlecry','', ''])
			#蓮華密使 : [x]<b>雄叫び:</b>ドルイド、ローグまたはシャーマンの_____カードを1枚<b>発見</b>する。
		elif ID == 'CFM_853':
			myCondition.append(['battlecry','', ''])
			#グライムストリートの運び屋 : <b>雄叫び:</b>自分の手札のランダムなミニオン1体に+1/+1を付与する。
		elif ID == 'CFM_855':
			myCondition.append(['battlecry','heHasDeathrattle(game)', 'silence'])
			#デファイアスの掃除屋 : [x]<b>雄叫び:</b><b>断末魔</b>を持つミニオン1体を<b>沈黙</b>させる。
	elif 'CS2_' in ID:
		if ID == 'CS2_117':
			myCondition.append(['battlecry','', ''])
			#大地の円環の遠見師 : <b>雄叫び:</b>体力を#3回復する。
		elif ID == 'CS2_141':
			myCondition.append(['battlecry','', ''])
			#アイアンフォージのライフル兵 : <b>雄叫び:</b> 1ダメージを与える。
		elif ID == 'CS2_147':
			myCondition.append(['battlecry','', ''])
			#ノームの発明家 : <b>雄叫び:</b> カードを1枚引く。
		elif ID == 'CS2_150':
			myCondition.append(['battlecry','', ''])
			#ストームパイクのコマンドー : <b>雄叫び:</b> 2ダメージを与える。
		elif ID == 'CS2_151':
			myCondition.append(['battlecry','', ''])
			#シルバーハンド騎士 : [x]<b>雄叫び:</b>2/2の従騎士を1体召喚する。
		elif ID == 'CS2_181':
			myCondition.append(['battlecry','', ''])
			#傷を負った剣匠 : <b>雄叫び:</b> 自身に4ダメージを与える。
		elif ID == 'CS2_188':
			myCondition.append(['battlecry','', ''])
			#鬼軍曹 : [x]<b>雄叫び:</b>このターンの間ミニオン1体に______攻撃力+2を付与する。_
		elif ID == 'CS2_189':
			myCondition.append(['battlecry','', ''])
			#エルフの射手 : <b>雄叫び:</b> 1ダメージを与える。
		elif ID == 'CS2_196':
			myCondition.append(['battlecry','', ''])
			#レイザーフェン・ハンター : [x]<b>雄叫び:</b> 1/1のイノシシを1体召喚する。
		elif ID == 'CS2_203':
			myCondition.append(['battlecry','heHasMinion(game)', 'silence'])
			#鉄嘴のフクロウ : [x]<b>雄叫び:</b>ミニオン1体を<b>沈黙</b>させる。
		elif ID == 'CS2_226':
			myCondition.append(['battlecry','', ''])
			#フロストウルフの将軍 : [x]<b>雄叫び:</b> 戦場にいる味方のミニオン1体につき____+1/+1を獲得する。
	elif 'DAL_' in ID:
		if ID == 'DAL_058':
			myCondition.append(['battlecry','', ''])
			#ヤジロボ : <b>挑発</b>、<b>雄叫び:</b>相手はデッキからミニオンを1体召喚する。
		elif ID == 'DAL_077':
			myCondition.append(['battlecry','', ''])
			#毒々フィン : [x]<b>雄叫び:</b>味方のマーロック1体に<b>猛毒</b>を付与する。
		elif ID == 'DAL_078':
			myCondition.append(['battlecry','', ''])
			#旅の治療師 : <b>聖なる盾</b>、<b>雄叫び:</b>体力を#3回復する。
		elif ID == 'DAL_081':
			myCondition.append(['battlecry','', ''])
			#魔除けの宝石職人 : [x]<b>雄叫び:</b>次の自分のターンまで自分のヒーローは呪文とヒーローパワーの標的にならない。
		elif ID == 'DAL_086':
			myCondition.append(['battlecry','', ''])
			#サンリーヴァーのスパイ : [x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合____+1/+1を獲得する。
		elif ID == 'DAL_087':
			myCondition.append(['battlecry','', ''])
			#ヘンチ・クランの妖婆 : [x]<b>雄叫び:</b>種族が「全て」である1/1の「融合体」を2体召喚する。
		elif ID == 'DAL_089':
			myCondition.append(['battlecry','', ''])
			#呪文書綴じ師 : [x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合____カードを1枚引く。
		elif ID == 'DAL_095':
			myCondition.append(['battlecry','', ''])
			#ヴァイオレット監獄の魔剣士 : [x]<b>雄叫び:</b>自分の手札の呪文1枚につき____攻撃力+1を獲得する。
		elif ID == 'DAL_400':
			myCondition.append(['battlecry','', ''])
			#悪党同盟の電線ネズミ : [x]<b>雄叫び:</b><b>悪の手先</b>1体を自分の手札に追加する。
		elif ID == 'DAL_416':
			myCondition.append(['battlecry','', ''])
			#ヘンチ・クランの強盗 : [x]<b>雄叫び:</b>他のクラスの呪文を1つ<b>発見</b>する。
		elif ID == 'DAL_417':
			myCondition.append(['battlecry','', ''])
			#強盗王トグワグル : [x]<b>雄叫び:</b>味方に<b>悪の手先</b>がいる場合、素敵な_____宝物を1つ選択する。
		elif ID == 'DAL_538':
			myCondition.append(['battlecry','', ''])
			#こっそり妨害工作員 : [x]<b>雄叫び:</b>相手は手札のランダムな呪文を1つ使用する。__<i>（対象はランダムに選択）</i>
		elif ID == 'DAL_539':
			myCondition.append(['battlecry','', ''])
			#サンリーヴァーの戦魔術師 : [x]<b>雄叫び:</b>自分の手札にコスト（5）以上の呪文がある場合__4ダメージを与える。
		elif ID == 'DAL_544':
			myCondition.append(['battlecry','', ''])
			#ポーション売り : [x]<b>雄叫び:</b>全ての味方のキャラクターの体力を#2回復する。
		elif ID == 'DAL_546':
			myCondition.append(['battlecry','', ''])
			#バリスタのリンチェン : [x]<b>雄叫び:</b>自身を除く味方の<b>雄叫び</b>を持つミニオン全てのコピーを1枚ずつ______自分の手札に追加する。_
		elif ID == 'DAL_554':
			myCondition.append(['battlecry','', ''])
			#シェフ・ノミ : [x]<b>雄叫び:</b>自分のデッキが空の場合6/6の「油火災のエレメンタル」を6体召喚する。
		elif ID == 'DAL_560':
			myCondition.append(['battlecry','', ''])
			#酒場のヒロイック女将 : [x]<b>挑発</b>、<b>雄叫び:</b>自身を除く味方のミニオン1体につき_____+2/+2を獲得する。_
		elif ID == 'DAL_565':
			myCondition.append(['battlecry','', ''])
			#ポータル・オーバーフィーンド : <b>雄叫び:</b>自分のデッキにポータル3枚を混ぜる。それを引いた際<b>急襲</b>を持つ2/2の悪魔を1体召喚する。
		elif ID == 'DAL_582':
			myCondition.append(['battlecry','', ''])
			#ポータルの番人 : <b>雄叫び:</b>自分のデッキにポータル3枚を混ぜる。それを引いた際<b>急襲</b>を持つ2/2の悪魔を1体召喚する。
		elif ID == 'DAL_714':
			myCondition.append(['battlecry','', ''])
			#最下層の故買屋 : [x]<b>雄叫び:</b>自分の手札に他のクラスのカードがある場合+1/+1と<b>急襲</b>を獲得する。
		elif ID == 'DAL_735':
			myCondition.append(['battlecry','HasNeedSilenceMinion', 'silence'])
			#ダラランの司書 : <b>雄叫び:</b>隣接するミニオンを<b>沈黙</b>させる。
		elif ID == 'DAL_736':
			myCondition.append(['battlecry','', ''])
			#文書管理官エリシアーナ : [x]<b>雄叫び:</b>カードを5枚<b>発見</b>する。そのコピー2枚ずつを自分のデッキと置き換える。
		elif ID == 'DAL_744':
			myCondition.append(['battlecry','', ''])
			#無貌レイジャー : [x]<b>雄叫び:</b>味方のミニオン1体の___体力をコピーする。
		elif ID == 'DAL_747':
			myCondition.append(['battlecry','', ''])
			#フライトマスター : [x]<b>雄叫び:</b>各プレイヤーの陣地に2/2の「グリフォン」を1体ずつ召喚する。
		elif ID == 'DAL_751':
			myCondition.append(['battlecry','', ''])
			#狂気の召喚師 : [x]<b>雄叫び:</b>各プレイヤーの陣地に1/1の「インプ」を____可能な限り召喚する。
		elif ID == 'DAL_752':
			myCondition.append(['battlecry','', ''])
			#ジェペット・ジョイバズ : [x]<b>雄叫び:</b>自分のデッキからミニオンを2体引く。それらの攻撃力、体力、コストを1に変える。
	elif 'DRG_' in ID:
		if ID == 'DRG_027':
			myCondition.append(['battlecry','', ''])
			#陰の殺し屋 : [x]<b>雄叫び:</b>既に2回<b>祈願</b>していた場合「コイン」3枚を____自分の手札に追加する。
		elif ID == 'DRG_034':
			myCondition.append(['battlecry','', ''])
			#密航者 : [x]<b>雄叫び:</b>自分のデッキに対戦開始時になかったカードがある場合、それらを2枚まで引く。
		elif ID == 'DRG_035':
			myCondition.append(['battlecry','', ''])
			#ブラッドセイルのスカイ賊 : [x]<b>雄叫び:</b>1/1の海賊2体を__自分の手札に追加する。
		elif ID == 'DRG_037':
			myCondition.append(['battlecry','', ''])
			#フリック・スカイシヴ : [x]<b>雄叫び:</b>ミニオン1体と同名のミニオン全てを破壊する<i>（居場所は問わない）</i>。
		elif ID == 'DRG_050':
			myCondition.append(['battlecry','', ''])
			#心血注ぐ献身者 : <b>急襲</b>、<b>雄叫び:</b>ガラクロンドに<b>祈願</b>する。
		elif ID == 'DRG_054':
			myCondition.append(['battlecry','', ''])
			#ぽっちゃりチビドラゴン : <b>雄叫び:</b>カードを1枚引く。
		elif ID == 'DRG_055':
			myCondition.append(['battlecry','', ''])
			#財宝荒らし : [x]<b>雄叫び:</b>自分の破壊された___武器1つを装備する。
		elif ID == 'DRG_059':
			myCondition.append(['battlecry','', ''])
			#ゴボグライダー技士 : [x]<b>雄叫び:</b>自分の陣地にメカがいる場合+1/+1と<b>急襲</b>を獲得する。
		elif ID == 'DRG_060':
			myCondition.append(['battlecry','', ''])
			#ファイアーホーク : [x]<b>雄叫び:</b>相手の手札1枚につき__攻撃力+1を獲得する。
		elif ID == 'DRG_062':
			myCondition.append(['battlecry','', ''])
			#ワームレストの浄術師 : [x]<b>雄叫び:</b>自分のデッキの中立カード全てをランダムな自分のクラスのカードに変身させる。
		elif ID == 'DRG_063':
			myCondition.append(['battlecry','', ''])
			#ドラゴンモーの密猟者 : <b>雄叫び:</b>相手の陣地にドラゴンがいる場合、+4/+4と<b>急襲</b>を獲得する。
		elif ID == 'DRG_064':
			myCondition.append(['battlecry','', ''])
			#ズルドラクの儀式官 : [x]<b>挑発</b>、<b>雄叫び:</b>ランダムなコスト1のミニオン3体を相手の______陣地に召喚する。__
		elif ID == 'DRG_067':
			myCondition.append(['battlecry','', ''])
			#トロルのコウモリ騎兵 : <b>雄叫び:</b>ランダムな敵のミニオン1体に__3ダメージを与える。
		elif ID == 'DRG_069':
			myCondition.append(['battlecry','', ''])
			#プレートブレイカー : [x]<b>雄叫び:</b>相手の装甲を破壊する。
		elif ID == 'DRG_070':
			myCondition.append(['battlecry','', ''])
			#ドラゴンブリーダー : <b>雄叫び:</b>味方のドラゴン1体を選択する。そのコピー1体を自分の手札に追加する。
		elif ID == 'DRG_072':
			myCondition.append(['battlecry','', ''])
			#スカイフィン : <b>雄叫び:</b>自分の手札にドラゴンがいる場合ランダムなマーロックを2体召喚する。
		elif ID == 'DRG_074':
			myCondition.append(['battlecry','', ''])
			#擬装した飛行船 : [x]<b>雄叫び:</b>次の自分のターンまで自身を除く味方のメカに<b>隠れ身</b>を付与する。
		elif ID == 'DRG_075':
			myCondition.append(['battlecry','', ''])
			#コバルト・スペルキン : [x]<b>雄叫び:</b>自分のクラスのコスト1の呪文2枚を自分の手札に追加する。
		elif ID == 'DRG_076':
			myCondition.append(['battlecry','', ''])
			#無貌の変性者 : <b>急襲</b>、<b>雄叫び:</b>味方のミニオン1体をこのミニオンのコピーに変身させる。
		elif ID == 'DRG_077':
			myCondition.append(['battlecry','', ''])
			#ウトガルドのグラップル狙撃手 : [x]<b>雄叫び:</b>両プレイヤーはカードを1枚引く。それがドラゴンだった場合召喚する。
		elif ID == 'DRG_081':
			myCondition.append(['battlecry','', ''])
			#スケイルライダー : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合_____2ダメージを与える。
		elif ID == 'DRG_082':
			myCondition.append(['battlecry','', ''])
			#コボルトの棒ドロ : <b>雄叫び:</b>相手の武器を奪う。
		elif ID == 'DRG_084':
			myCondition.append(['battlecry','', ''])
			#触手の脅異 : [x]<b>雄叫び:</b>各プレイヤーはカードを1枚ずつ引く。それらの____コストを入れ替える。__
		elif ID == 'DRG_086':
			myCondition.append(['battlecry','', ''])
			#クロマティックの卵 : [x]<b>雄叫び:</b>孵化後のドラゴン1体を秘密裏に<b>発見</b>する。__<b>断末魔:</b>_孵化する！
		elif ID == 'DRG_089':
			myCondition.append(['battlecry','', ''])
			#竜の女王アレクストラーザ : [x]<b>雄叫び:</b>_自分のデッキに重複するカードがない場合自身を除くランダムなドラゴン2体を自分の手札に追加する。____それらのコストは（1）になる。
		elif ID == 'DRG_099':
			myCondition.append(['battlecry','', ''])
			#クロンクス・ドラゴンフーフ : [x]<b>雄叫び:</b>ガラクロンドを引く。自分が既にガラクロンドの場合ガラクロンドの大禍を引き起こす。
		elif ID == 'DRG_213':
			myCondition.append(['battlecry','', ''])
			#双暴帝 : [x]<b>雄叫び:</b>ランダムな敵のミニオン2体に_____4ダメージずつ与える。
		elif ID == 'DRG_242':
			myCondition.append(['battlecry','', ''])
			#ガラクロンドの盾 : <b>挑発</b>、<b>雄叫び:</b>ガラクロンドに<b>祈願</b>する。
		elif ID == 'DRG_257':
			myCondition.append(['battlecry','', ''])
			#フリズ・キンドルルースト : <b>雄叫び:</b>自分のデッキのドラゴン全てのコストを（2）減らす。
		elif ID == 'DRG_401':
			myCondition.append(['battlecry','', ''])
			#灰色の魔法使い : [x]<b>雄叫び:</b>次の自分のターンまで相手とヒーロー______パワーを交換する。_
		elif ID == 'DRG_402':
			myCondition.append(['battlecry','', ''])
			#サスロヴァール : [x]<b>雄叫び:</b>味方のミニオン1体を選択。そのミニオンのコピーを自分の手札、デッキ、陣地に_____それぞれ1体ずつ追加する。
		elif ID == 'DRG_403':
			myCondition.append(['battlecry','', ''])
			#ブロートーチ妨害工作員 : <b>雄叫び:</b>相手が次に使うヒーローパワーのコストは（3）。
	elif ID == 'DS1_055':
			myCondition.append(['battlecry','', ''])
			#ダークスケイルの治療師 : <b>雄叫び:</b>全ての味方のキャラクターの体力を#2回復する。
	elif 'EX1_' in ID:
		if ID == 'EX1_002':
			myCondition.append(['battlecry','', ''])
			#黒騎士 : [x]<b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を破壊する。
		elif ID == 'EX1_005':
			myCondition.append(['battlecry','', ''])
			#大物ハンター : [x]<b>雄叫び:</b>攻撃力7以上のミニオン1体を破壊する。
		elif ID == 'EX1_011':
			myCondition.append(['battlecry','', ''])
			#ヴードゥーの呪術医 : <b>雄叫び:</b>体力を#2回復する。
		elif ID == 'EX1_014':
			myCondition.append(['battlecry','', ''])
			#キング・ムクラ : <b>雄叫び:</b> 敵の手札に「バナナ」2枚を追加する。
		elif ID == 'EX1_015':
			myCondition.append(['battlecry','', ''])
			#初級エンジニア : <b>雄叫び:</b> カードを1枚引く。
		elif ID == 'EX1_019':
			myCondition.append(['battlecry','', ''])
			#シャタード・サンの聖職者 : [x]<b>雄叫び:</b>味方のミニオン1体に +1/+1を 付与する。
		elif ID == 'EX1_025':
			myCondition.append(['battlecry','', ''])
			#ミニドラゴン・メカニック : [x]<b>雄叫び:</b> 2/1のメカ・ミニドラゴンを[b]1体召喚する。
		elif ID == 'EX1_043':
			myCondition.append(['battlecry','', ''])
			#トワイライト・ドレイク : <b>雄叫び:</b> 自分の手札1枚につき体力+1を獲得する。
		elif ID == 'EX1_046':
			myCondition.append(['battlecry','', ''])
			#ダークアイアンのドワーフ : [x]<b>雄叫び:</b> このターンの間ミニオン1体に　攻撃力+2を付与する。
		elif ID == 'EX1_048':
			myCondition.append(['battlecry','heHasNonVanilla(game)', 'silence'])
			#スペルブレイカー : [x]<b>雄叫び:</b>ミニオン1体を<b>沈黙</b>させる。
		elif ID == 'EX1_049':
			myCondition.append(['battlecry','', ''])
			#若き酒造大師 : <b>雄叫び:</b> 味方のミニオン1体を戦場から自分の手札に戻す。
		elif ID == 'EX1_050':
			myCondition.append(['battlecry','', ''])
			#コールドライトの託宣師 : [x]<b>雄叫び:</b> 各プレイヤーはカードを2枚ずつ引く。
		elif ID == 'EX1_057':
			myCondition.append(['battlecry','', ''])
			#老練の酒造大師 : <b>雄叫び:</b> 味方のミニオン1体を戦場から自分の手札に戻す。
		elif ID == 'EX1_058':
			myCondition.append(['battlecry','', ''])
			#サンフューリーの護衛 : [x]<b>雄叫び:</b> 隣接するミニオンに<b>挑発</b>を付与する。
		elif ID == 'EX1_059':
			myCondition.append(['battlecry','', ''])
			#イカレた錬金術師 : [x]<b>雄叫び:</b> ミニオン1体の攻撃力と体力を入れ替える。
		elif ID == 'EX1_066':
			myCondition.append(['battlecry','', ''])
			#酸性沼ウーズ : <b>雄叫び:</b> 敵の武器を破壊する。
		elif ID == 'EX1_082':
			myCondition.append(['battlecry','', ''])
			#マッドボンバー : [x]<b>雄叫び:</b>合計3ダメージを自身を除くキャラクターに____ランダムに振り分ける。
		elif ID == 'EX1_083':
			myCondition.append(['battlecry','', ''])
			#ティンクマスター・オーバースパーク : [x]<b>雄叫び:</b> 自身以外のランダムなミニオン1体を5/5のデビルサウルスか_____1/1のリスに変身させる。_
		elif ID == 'EX1_085':
			myCondition.append(['battlecry','', ''])
			#精神支配技士 : [x]<b>雄叫び:</b> 戦場に敵のミニオンが4体以上いる場合ランダムな1体を自分の味方にする。
		elif ID == 'EX1_089':
			myCondition.append(['battlecry','', ''])
			#魔力のゴーレム : [x]<b>雄叫び:</b>相手にマナクリスタルを1個付与する。
		elif ID == 'EX1_093':
			myCondition.append(['battlecry','', ''])
			#アルガスの守護者 : <b>雄叫び:</b> 隣接するミニオンに+1/+1と<b>挑発</b>を付与する。
		elif ID == 'EX1_103':
			myCondition.append(['battlecry','', ''])
			#コールドライトの予言者 : [x]<b>雄叫び:</b> 自身を除く味方のマーロックに_____体力+2を付与する。
		elif ID == 'EX1_112':
			myCondition.append(['battlecry','', ''])
			#ゲルビン・メカトルク : <b>雄叫び:</b> すばらしい発明品を1体召喚する。
		elif ID == 'EX1_116':
			myCondition.append(['battlecry','', ''])
			#リロイ・ジェンキンス : [x]<b>突撃</b>、<b>雄叫び:</b> 敵の陣地に1/1のチビドラゴンを2体召喚する。
		elif ID == 'EX1_133':
			myCondition.append(['battlecry','', ''])
			#地獄送りの刃 : [x]<b>雄叫び:</b>_____1ダメージを与える。__ <b>コンボ:</b> 代わりに________2ダメージを与える。
		elif ID == 'EX1_186':
			myCondition.append(['battlecry','', ''])
			#SI:7潜入工作員 : [x]<b>雄叫び:</b>ランダムな敵の___<b>秘策</b>1つを破壊する。
		elif ID == 'EX1_188':
			myCondition.append(['battlecry','', ''])
			#荒野の口取り : [x]<b>雄叫び:</b>ランダムな獣を1体召喚する。
		elif ID == 'EX1_189':
			myCondition.append(['battlecry','', ''])
			#ブライトウィング : <b>雄叫び:</b>ランダムな<b>レジェンド</b>ミニオン1体を自分の手札に追加する。
		elif ID == 'EX1_190':
			myCondition.append(['battlecry','', ''])
			#大審問官ホワイトメイン : <b>雄叫び:</b>このターンに死亡した味方のミニオン全てを召喚する。
		elif ID == 'EX1_191':
			myCondition.append(['battlecry','', ''])
			#病魔の運び手 : [x]<b>雄叫び:</b>味方のミニオン1体に<b>猛毒</b>を付与する。
		elif ID == 'EX1_283':
			myCondition.append(['battlecry','', ''])
			#フロスト・エレメンタル : [x]<b>雄叫び:</b> キャラクター1体を<b>凍結</b>させる。
		elif ID == 'EX1_284':
			myCondition.append(['battlecry','', ''])
			#アジュア・ドレイク : [x]<b>呪文ダメージ+1</b><b>雄叫び:</b>カードを1枚引く。
		elif ID == 'EX1_506':
			myCondition.append(['battlecry','', ''])
			#マーロックのタイドハンター : [x]<b>雄叫び:</b> 1/1のマーロックの 偵察兵を1体召喚する。
		elif ID == 'EX1_558':
			myCondition.append(['battlecry','', ''])
			#ハリソン・ジョーンズ : <b>雄叫び:</b> 敵の武器を破壊しその耐久度に等しい枚数のカードを引く。
		elif ID == 'EX1_561':
			myCondition.append(['battlecry','', ''])
			#アレクストラーザ : [x]<b>雄叫び:</b>ヒーロー1人の残り__体力を15にする。
		elif ID == 'EX1_562':
			myCondition.append(['battlecry','', ''])
			#オニクシア : [x]<b>雄叫び:</b>自分の陣地が満員になる数の1/1のチビドラゴンを召喚する。
		elif ID == 'EX1_564':
			myCondition.append(['battlecry','', ''])
			#無貌の操り手 : <b>雄叫び:</b> ミニオン1体を選択しそのミニオンのコピーに変化する。
		elif ID == 'EX1_583':
			myCondition.append(['battlecry','', ''])
			#エルーンのプリーステス : <b>雄叫び:</b>自分のヒーローの体力を#4回復する。
		elif ID == 'EX1_584':
			myCondition.append(['battlecry','', ''])
			#老練のメイジ : [x]<b>雄叫び:</b> 隣接するミニオンに<b>呪文ダメージ+1</b>を付与する。
		elif ID == 'EX1_590':
			myCondition.append(['battlecry','', ''])
			#ブラッドナイト : [x]<b>雄叫び:</b> 全てのミニオンは<b>聖なる盾</b>を失う。失われた聖なる盾1つにつき+3/+3を獲得する。
		elif ID == 'EX1_593':
			myCondition.append(['battlecry','', ''])
			#ナイトブレード : [x]<b>雄叫び: </b>敵のヒーローに3ダメージを与える。
	elif 'FP1_' in ID:
		if ID == 'FP1_003':
			myCondition.append(['battlecry','', ''])
			#反響ウーズ : <b>雄叫び:</b> このターンの終了時にこのミニオンと全く同じコピーを1体召喚する。
		elif ID == 'FP1_016':
			myCondition.append(['battlecry','HasNeedSilenceMinion', 'silence'])
			#泣き叫ぶ魂 : [x]<b>雄叫び: </b>自身を除く味方のミニオンを_____<b>沈黙</b>させる。
		elif ID == 'FP1_030':
			myCondition.append(['battlecry','', ''])
			#ロウゼブ : <b>雄叫び:</b> 次のターン敵の呪文のコストが（5）増える。
	elif 'GIL_' in ID:
		if ID == 'GIL_124':
			myCondition.append(['battlecry','', ''])
			#苔むしたモノノケ : [x]<b>雄叫び:</b>自身を除く攻撃力2以下のミニオンを全て破壊する。
		elif ID == 'GIL_125':
			myCondition.append(['battlecry','', ''])
			#いかれ帽子屋 : [x]<b>雄叫び:</b>自身を除くミニオンに帽子を3個ランダムに投げる。帽子はそれぞれ+1/+1を付与する。
		elif ID == 'GIL_198':
			myCondition.append(['battlecry','', ''])
			#アザリナ・ソウルシーフ : [x]<b>雄叫び:</b>自分の手札全てを相手の手札全てのコピーに置き換える。
		elif ID == 'GIL_212':
			myCondition.append(['battlecry','', ''])
			#鴉使い : [x]<b>雄叫び:</b>ランダムなコスト1のミニオン2体を自分の手札に追加する。
		elif ID == 'GIL_213':
			myCondition.append(['battlecry','', ''])
			#毛むくじゃらのミスティック : [x]<b>雄叫び:</b>ランダムなコスト2の___ミニオン1体を各プレイヤーの手札に追加する。
		elif ID == 'GIL_526':
			myCondition.append(['battlecry','', ''])
			#ワームガード : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>挑発</b>を獲得する。
		elif ID == 'GIL_561':
			myCondition.append(['battlecry','', ''])
			#ブラックワルド・ピクシー : [x]<b>雄叫び:</b>自分のヒーローパワーを再度使用可能にする。
		elif ID == 'GIL_578':
			myCondition.append(['battlecry','', ''])
			#アッシュモア伯爵夫人 : [x]<b>雄叫び:</b>自分のデッキから<b>急襲</b><b>生命奪取</b>、<b>断末魔</b>を持つカードをそれぞれ1枚引く。
		elif ID == 'GIL_581':
			myCondition.append(['battlecry','', ''])
			#サンドバインダー : [x]<b>雄叫び:</b>自分のデッキからエレメンタル_を1体引く。
		elif ID == 'GIL_584':
			myCondition.append(['battlecry','', ''])
			#ウィッチウッドの笛吹き : [x]<b>雄叫び:</b>自分のデッキから最もコストが低い____ミニオンを1体引く。
		elif ID == 'GIL_598':
			myCondition.append(['battlecry','', ''])
			#テス・グレイメイン : [x]<b>雄叫び:</b>この対戦で自分が手札から使用した他のクラスのカード全てを再度使用する<i>（対象はランダムに選択される）</i>。
		elif ID == 'GIL_601':
			myCondition.append(['battlecry','', ''])
			#スケイルワーム : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>急襲</b>を獲得する。
		elif ID == 'GIL_614':
			myCondition.append(['battlecry','', ''])
			#ヴードゥー人形 : [x]<b>雄叫び:</b>ミニオン1体を選択する。<b>断末魔:</b>選択したミニオンを破壊する。
		elif ID == 'GIL_622':
			myCondition.append(['battlecry','', ''])
			#ライフドリンカー : [x]<b>雄叫び:</b>敵のヒーローに3ダメージを与える。自分のヒーローの体力を#3回復する。
		elif ID == 'GIL_623':
			myCondition.append(['battlecry','', ''])
			#ウィッチウッドのグリズリー : [x]<b>挑発</b>、<b>雄叫び:</b>相手の手札1枚につき___体力を1失う。
		elif ID == 'GIL_624':
			myCondition.append(['battlecry','', ''])
			#ナイトプロウラー : [x]<b>雄叫び:</b>戦場に他のミニオンがいない場合、+3/+3を獲得する。
		elif ID == 'GIL_648':
			myCondition.append(['battlecry','', ''])
			#ギルニーアスの警部 : <b>雄叫び:</b>敵の<b>秘策</b>全てを破壊する。
		elif ID == 'GIL_677':
			myCondition.append(['battlecry','', ''])
			#貌を蒐めるもの : [x]<b>木霊</b>、<b>雄叫び:</b>ランダムな<b>レジェンド</b>ミニオン1体を自分の手札に追加する。
		elif ID == 'GIL_682':
			myCondition.append(['battlecry','', ''])
			#マックハンター : [x]<b>急襲</b>、<b>雄叫び:</b>相手の陣地に2/1の「マックリング」_を2体召喚する。
		elif ID == 'GIL_683':
			myCondition.append(['battlecry','', ''])
			#沼地のドレイク : [x]<b>雄叫び:</b>相手の陣地に<b>猛毒</b>を持つ2/1の「ドレイクスレイヤー」を1体召喚する。
		elif ID == 'GIL_815':
			myCondition.append(['battlecry','', ''])
			#悪意の銀行家 : [x]<b>雄叫び:</b>味方のミニオン1体を選択する。そのコピー1体を___自分のデッキに混ぜる。
		elif ID == 'GIL_827':
			myCondition.append(['battlecry','', ''])
			#ブリンク・フォックス : [x]<b>雄叫び:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。
	elif 'GVG_' in ID:
		if ID == 'GVG_023':
			myCondition.append(['battlecry','', ''])
			#ゴブリン式全自動散髪機 : [x]<b>雄叫び:</b> 自分の武器に攻撃力+1を__付与する。
		elif ID == 'GVG_069':
			myCondition.append(['battlecry','', ''])
			#骨董品のヒールロボ : <b>雄叫び:</b>自分のヒーローの体力を#8回復する。
		elif ID == 'GVG_074':
			myCondition.append(['battlecry','', ''])
			#ケザンのミスティック : <b>雄叫び:</b> 敵のランダムな<b>秘策</b>1つを自分のものにする。
		elif ID == 'GVG_090':
			myCondition.append(['battlecry','', ''])
			#マッダーボンバー : [x]<b>雄叫び:</b>合計6ダメージを自身を除くキャラクターに____ランダムに振り分ける。
		elif ID == 'GVG_092':
			myCondition.append(['battlecry','', ''])
			#ノームの実験者 : [x]<b>雄叫び:</b> カードを1枚引く。そのカードがミニオンだった場合、そのカードを________ニワトリに変身させる。__
		elif ID == 'GVG_097':
			myCondition.append(['battlecry','', ''])
			#リトル・エクソシスト : [x]<b>挑発</b>、<b>雄叫び:</b> <b>断末魔</b>を持つ敵のミニオン1体につき_____+1/+1を獲得する。_
		elif ID == 'GVG_099':
			myCondition.append(['battlecry','', ''])
			#ボム・ロバー : <b>雄叫び:</b> ランダムな敵のミニオン1体に4ダメージを与える。
		elif ID == 'GVG_102':
			myCondition.append(['battlecry','', ''])
			#ティンカータウンの技術者 : <b>雄叫び:</b> 味方にメカがいる場合+1/+1を獲得しさらに自分の手札に<b>スペアパーツ</b>1枚を追加する。
		elif ID == 'GVG_107':
			myCondition.append(['battlecry','', ''])
			#エンハンス・オ・メカーノ : <b>雄叫び:</b> 自身を除く味方のミニオンに<b>疾風</b>、<b>挑発</b>または___<b>聖なる盾</b>を付与する<i>（どれが付与されるかはランダム）。</i>
		elif ID == 'GVG_108':
			myCondition.append(['battlecry','', ''])
			#リコンボビュレイター : [x]<b>雄叫び:</b> 味方のミニオン1体を、ランダムな同コストのミニオンに変身させる。
		elif ID == 'GVG_110':
			myCondition.append(['battlecry','', ''])
			#ドクター・ブーム : <b>雄叫び:</b> 1/1のブームロボを2体召喚する。<i>警告: ロボは爆発する場合がある。</i>
		elif ID == 'GVG_119':
			myCondition.append(['battlecry','', ''])
			#ブリングトロン3000 : <b>雄叫び:</b> 各プレイヤーはランダムな武器を装備する。
		elif ID == 'GVG_120':
			myCondition.append(['battlecry','', ''])
			#ヒーメット・ネッシングウェアリー : <b>雄叫び:</b> 獣1体を破壊する。
	elif 'ICC_' in ID:
		if ID == 'ICC_018':
			myCondition.append(['battlecry','', ''])
			#ぶんどり幽霊船員 : [x]<b>雄叫び:</b>自分の武器の値に等しい攻撃力と　体力を獲得する。
		elif ID == 'ICC_025':
			myCondition.append(['battlecry','', ''])
			#ガラガラガイコツ : [x]<b>雄叫び:</b>5/5のスケルトンを1体召喚する。<b>断末魔:</b>5/5のスケルトンを1体敵の陣地に召喚する。
		elif ID == 'ICC_026':
			myCondition.append(['battlecry','', ''])
			#非情の死霊術師 : [x]<b>雄叫び:</b>1/1のスケルトンを2体召喚する。
		elif ID == 'ICC_028':
			myCondition.append(['battlecry','', ''])
			#サンボーン・ヴァルキル : [x]<b>雄叫び:</b>隣接するミニオンに　体力+2を付与する。
		elif ID == 'ICC_092':
			myCondition.append(['battlecry','', ''])
			#アケラスの古残兵 : <b>雄叫び:</b>味方のミニオン1体に攻撃力+1を付与する。
		elif ID == 'ICC_093':
			myCondition.append(['battlecry','', ''])
			#タスカーの漁師 : [x]<b>雄叫び:</b>味方のミニオン1体に<b>呪文ダメージ+1</b>を付与する。
		elif ID == 'ICC_094':
			myCondition.append(['battlecry','', ''])
			#フォールン・サンの聖職者 : [x]<b>雄叫び:</b>味方のミニオン1体に　+1/+1を付与する。
		elif ID == 'ICC_096':
			myCondition.append(['battlecry','', ''])
			#タタラボッチ : <b>雄叫び:</b>自分の手札の武器を全て破棄しそれらの攻撃力と耐久度を獲得する。
		elif ID == 'ICC_098':
			myCondition.append(['battlecry','', ''])
			#墓に潜むもの : [x]<b>雄叫び:</b>この対戦で死亡した<b>断末魔</b>を持つミニオンをランダムに1体自分の手札に追加する。
		elif ID == 'ICC_257':
			myCondition.append(['battlecry','', ''])
			#死体蘇生者 : [x]<b>雄叫び:</b>味方のミニオン1体に「<b>断末魔:</b> このミニオンを再度召喚する」を付与する。
		elif ID == 'ICC_466':
			myCondition.append(['battlecry','', ''])
			#サロナイト鉱山の奴隷 : [x]<b>挑発</b><b>雄叫び:</b>「サロナイト鉱山の奴隷」をもう1体召喚する。
		elif ID == 'ICC_467':
			myCondition.append(['battlecry','', ''])
			#ネルビアンの説凶師 : [x]<b>雄叫び:</b>味方のミニオン1体にこのターンの間<b>無敵</b>を付与する。
		elif ID == 'ICC_701':
			myCondition.append(['battlecry','', ''])
			#待ち伏せのガイスト : <b>雄叫び:</b>両プレイヤーの手札とデッキのコスト1の呪文を全て破壊する。
		elif ID == 'ICC_705':
			myCondition.append(['battlecry','', ''])
			#ボーンメア : [x]<b>雄叫び:</b>味方のミニオン1体に+4/+4と<b>挑発</b>を付与する。
		elif ID == 'ICC_810':
			myCondition.append(['battlecry','', ''])
			#斧死なる断罪者 : [x]<b>雄叫び:</b>自分の手札の<b>生命奪取</b>を持つランダムなミニオン1体に+2/+2を付与する。
		elif ID == 'ICC_811':
			myCondition.append(['battlecry','', ''])
			#リリアン・ヴォス : [x]<b>雄叫び:</b>自分の手札の呪文全てを<i>相手のクラスの</i>ランダムな呪文と置き換える。
		elif ID == 'ICC_850':
			myCondition.append(['battlecry','', ''])
			#シャドウブレード : [x]<b>雄叫び:</b>自分のヒーローはこのターンの間<b>無敵</b>。
		elif ID == 'ICC_851':
			myCondition.append(['battlecry','', ''])
			#ケレセス公爵 : [x]<b>雄叫び:</b>自分のデッキにコスト2のカードがない場合、自分のデッキのミニオン全てに+1/+1を付与する。
		elif ID == 'ICC_852':
			myCondition.append(['battlecry','', ''])
			#タルダラム公爵 : [x]<b>雄叫び:</b>自分のデッキにコスト3のカードがない場合選択したミニオンの3/3のコピーに変身する。
		elif ID == 'ICC_853':
			myCondition.append(['battlecry','', ''])
			#ヴァラナール公爵 : [x]<b>雄叫び:</b>自分のデッキにコスト4のカードがない場合<b>生命奪取</b>と<b>挑発</b>を獲得する。
		elif ID == 'ICC_855':
			myCondition.append(['battlecry','', ''])
			#ヒルドニル・フロストライダール : <b>雄叫び:</b>自身を除く味方のミニオンを<b>凍結</b>させる。
		elif ID == 'ICC_904':
			myCondition.append(['battlecry','', ''])
			#骸骨の魔女 : [x]<b>雄叫び:</b>このターンに死亡したミニオン1体につき　+1/+1を獲得する。
		elif ID == 'ICC_912':
			myCondition.append(['battlecry','', ''])
			#躯の駆り手 : [x]<b>雄叫び:</b><b>挑発</b>を持つミニオンが自分のデッキにある場合、<b>挑発</b>を獲得。同様に<b>聖なる盾</b>、<b>生命奪取</b>、<b>疾風</b>も獲得可能。
	elif 'KAR_' in ID:
		if ID == 'KAR_030a':
			myCondition.append(['battlecry','', ''])
			#食糧庫蜘蛛 : <b>雄叫び:</b>1/3の蜘蛛を1体召喚する。
		elif ID == 'KAR_033':
			myCondition.append(['battlecry','', ''])
			#ブック・ワーム : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力3以下の敵の______ミニオン1体を破壊する。_
		elif ID == 'KAR_037':
			myCondition.append(['battlecry','', ''])
			#番鳥 : <b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合、+1/+1と<b>挑発</b>を獲得する。
		elif ID == 'KAR_041':
			myCondition.append(['battlecry','', ''])
			#堀に潜むもの : <b>雄叫び:</b>ミニオン1体を破壊する。<b>断末魔:</b>破壊したミニオンを再度召喚する。
		elif ID == 'KAR_061':
			myCondition.append(['battlecry','', ''])
			#キュレーター : [x]<b>挑発</b>、<b>雄叫び:</b>自分のデッキから獣、ドラゴン、マーロックを1体ずつ引く。
		elif ID == 'KAR_062':
			myCondition.append(['battlecry','', ''])
			#ネザースパイトの歴史家 : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合____ドラゴン1体を<b>発見</b>する。
		elif ID == 'KAR_069':
			myCondition.append(['battlecry','', ''])
			#怪盗紳士 : [x]<b>雄叫び:</b><i>相手のクラスの</i>ランダムなカード1枚を_____自分の手札に追加する。
		elif ID == 'KAR_070':
			myCondition.append(['battlecry','', ''])
			#イセリアルの売人 : [x]<b>雄叫び:</b>自分の手札に他のクラスのカードがある場合それらのコストを（2）減らす。
		elif ID == 'KAR_095':
			myCondition.append(['battlecry','', ''])
			#動物園ロボ : [x]<b>雄叫び:</b>ランダムな味方の獣、ドラゴン、マーロック1体にそれぞれ+1/+1を付与する。
		elif ID == 'KAR_097':
			myCondition.append(['battlecry','', ''])
			#ガーディアン・メディヴ : [x]<b>雄叫び:</b>ガーディアンの大杖__アティシュを装備する。
		elif ID == 'KAR_114':
			myCondition.append(['battlecry','', ''])
			#バーンズ : <b>雄叫び:</b>自分のデッキのランダムなミニオンの1/1のコピーを[x]1体召喚する。
		elif ID == 'KAR_702':
			myCondition.append(['battlecry','', ''])
			#動物園の奇術師 : [x]<b>雄叫び:</b>ランダムな味方の獣、ドラゴン、マーロック1体にそれぞれ+2/+2を付与する。
		elif ID == 'KAR_710':
			myCondition.append(['battlecry','', ''])
			#魔力細工師 : <b>雄叫び:</b><b>挑発</b>を持つ0/5のミニオンを1体召喚する。
	elif 'LOE_' in ID:
		if ID == 'LOE_011':
			myCondition.append(['battlecry','', ''])
			#レノ・ジャクソン : [x]<b>雄叫び:</b>自分のデッキに重複するカードがない場合自分のヒーローの体力を完全に回復する。
		elif ID == 'LOE_019':
			myCondition.append(['battlecry','', ''])
			#掘り起こされたラプター : [x]<b>雄叫び:</b> 味方のミニオン1体を選択する。そのミニオンの____<b>断末魔</b>の能力をコピーする。
		elif ID == 'LOE_029':
			myCondition.append(['battlecry','', ''])
			#宝飾のスカラベ : [x]<b>雄叫び:</b> コスト3の　カード1枚を<b>発見</b>する。
		elif ID == 'LOE_039':
			myCondition.append(['battlecry','', ''])
			#ゴリラロボA-3 : [x]<b>雄叫び:</b>味方に別のメカがいる場合メカ1体を<b>発見</b>する。
		elif ID == 'LOE_047':
			myCondition.append(['battlecry','', ''])
			#墓守蜘蛛 : <b>雄叫び:</b> 獣1体を<b>発見</b>する。
		elif ID == 'LOE_073':
			myCondition.append(['battlecry','', ''])
			#デビルサウルスの化石 : <b>雄叫び:</b> 味方に獣がいる場合<b>挑発</b>を獲得する。
		elif ID == 'LOE_076':
			myCondition.append(['battlecry','', ''])
			#サー・フィンレー・マルグルトン : <b>雄叫び:</b>新たな基本ヒーローパワー1つを<b>発見</b>する。
		elif ID == 'LOE_079':
			myCondition.append(['battlecry','', ''])
			#エリーズ・スターシーカー : [x]<b>雄叫び:</b> 自分のデッキに「黄金のサルへの地図」1枚を混ぜる。
		elif ID == 'LOE_092':
			myCondition.append(['battlecry','', ''])
			#大怪盗ラファーム : <b>雄叫び:</b> 強力な秘宝を1つ<b>発見</b>する。
		elif ID == 'LOE_110':
			myCondition.append(['battlecry','', ''])
			#古代のシェード : [x]<b>雄叫び:</b>自分のデッキに「古代の呪い」1枚を混ぜる。「古代の呪い」を引くと_____自分が7ダメージを受ける。
	elif 'LOOT_' in ID:
		if ID == 'LOOT_026':
			myCondition.append(['battlecry','', ''])
			#ファルドライ・ストライダー : [x]<b>雄叫び:</b> 自分のデッキに待ち伏せ！3枚を混ぜる。待ち伏せ！を引いた際自分の陣地に4/4のクモを1体召喚する。
		elif ID == 'LOOT_033':
			myCondition.append(['battlecry','', ''])
			#大洞窟のキラキラ拾い : [x]<b>雄叫び:</b>自分のデッキから武器を1枚引く。
		elif ID == 'LOOT_069':
			myCondition.append(['battlecry','', ''])
			#下水さらい : [x]<b>雄叫び:</b>2/3の「巨大ネズミ」を1体召喚する。
		elif ID == 'LOOT_111':
			myCondition.append(['battlecry','', ''])
			#スコーピ・オ・マティック : <b>雄叫び:</b>攻撃力1以下のミニオン1体を破壊する。
		elif ID == 'LOOT_118':
			myCondition.append(['battlecry','', ''])
			#漆黒のドラゴン鍛冶 : <b>雄叫び:</b>自分の手札のランダムな武器1つのコストを（2）減らす。
		elif ID == 'LOOT_122':
			myCondition.append(['battlecry','', ''])
			#腐蝕ヘドロ : <b>雄叫び:</b>敵の武器を破壊する。
		elif ID == 'LOOT_124':
			myCondition.append(['battlecry','', ''])
			#孤高の勇者 : [x]<b>雄叫び:</b>味方に他のミニオンがいない場合、<b>聖なる盾</b>と<b>挑発</b>を獲得する。
		elif ID == 'LOOT_132':
			myCondition.append(['battlecry','', ''])
			#ドラゴンスレイヤー : <b>雄叫び:</b>ドラゴン1体に6ダメージを与える。
		elif ID == 'LOOT_150':
			myCondition.append(['battlecry','', ''])
			#ファーボルグの苔編み師 : [x]<b>雄叫び:</b>味方のミニオン1体を__6/6のエレメンタルに__変身させる。
		elif ID == 'LOOT_152':
			myCondition.append(['battlecry','', ''])
			#賑やかな吟遊詩人 : <b>雄叫び:</b>自身を除く味方のミニオンに体力+1を付与する。
		elif ID == 'LOOT_154':
			myCondition.append(['battlecry','', ''])
			#ジャリッパナの騎士 : [x]<b>雄叫び:</b>ランダムなコスト1のミニオン1体を____相手の陣地に召喚する。
		elif ID == 'LOOT_161':
			myCondition.append(['battlecry','', ''])
			#肉食キューブ : [x]<b>雄叫び:</b>味方のミニオン1体を破壊。<b>断末魔:</b>そのミニオンのコピーを2体召喚する。
		elif ID == 'LOOT_167':
			myCondition.append(['battlecry','', ''])
			#菌術師 : [x]<b>雄叫び:</b>隣接するミニオンに__+2/+2を付与する。
		elif ID == 'LOOT_291':
			myCondition.append(['battlecry','', ''])
			#キノコ酒造師 : <b>雄叫び:</b>体力を#4回復する。
		elif ID == 'LOOT_347':
			myCondition.append(['battlecry','', ''])
			#コボルトの弟子 : [x]<b>雄叫び:</b>合計3ダメージを敵にランダムに振り分ける。
		elif ID == 'LOOT_357':
			myCondition.append(['battlecry','', ''])
			#狐のマリン : [x]<b>雄叫び:</b>相手の陣地に0/8の宝箱を1個召喚する。____<i>(破壊するとお宝入手！)_</i>
		elif ID == 'LOOT_375':
			myCondition.append(['battlecry','', ''])
			#ギルド募集係 : <b>雄叫び:</b>コスト（4）以下のミニオンを1体<b>招集</b>する。
		elif ID == 'LOOT_383':
			myCondition.append(['battlecry','', ''])
			#飢えているエティン : <b>挑発</b>、<b>雄叫び:</b>ランダムなコスト2のミニオン1体を相手の陣地に召喚する。
		elif ID == 'LOOT_388':
			myCondition.append(['battlecry','', ''])
			#キノコの呪い師 : <b>雄叫び:</b>全ての味方のキャラクターの体力を#2回復する。
		elif ID == 'LOOT_389':
			myCondition.append(['battlecry','', ''])
			#クズ拾いのコボルト : <b>雄叫び:</b>自分の破壊された武器1つを自分の手札に戻す。
		elif ID == 'LOOT_516':
			myCondition.append(['battlecry','', ''])
			#ゴルゴン・ゾーラ : [x]<b>雄叫び:</b>味方のミニオン1体を選択。そのミニオンのゴールデンのコピー1体を自分の手札に追加する。
		elif ID == 'LOOT_521':
			myCondition.append(['battlecry','', ''])
			#マスター・オークハート : [x]<b>雄叫び:</b>攻撃力1、2、3のミニオンを1体ずつ<b>招集</b>する。
		elif ID == 'LOOT_526':
			myCondition.append(['battlecry','', ''])
			#クライヤミ : [x]最初は<b>休眠状態</b>。<b>雄叫び:</b>_相手のデッキにロウソク3枚を混ぜる。それらが全て引かれるとこれは目覚める。
		elif ID == 'LOOT_529':
			myCondition.append(['battlecry','', ''])
			#ヴォイド・リッパー : <b>雄叫び:</b>自身を除く全てのミニオンの攻撃力と体力を入れ替える。
		elif ID == 'LOOT_539':
			myCondition.append(['battlecry','', ''])
			#性悪な召喚師 : [x]<b>雄叫び:</b>自分のデッキの呪文を1枚表示する。その呪文と同じコストのランダムな____ミニオン1体を召喚する。
		elif ID == 'LOOT_541':
			myCondition.append(['battlecry','', ''])
			#キング・トグワグル : [x]<b>雄叫び:</b>相手とデッキを交換する。再度交換するための身代金の呪文1枚を相手に与える。
	elif 'NEW_' in ID:
		if ID == 'NEW1_014':
			myCondition.append(['battlecry','', ''])
			#変装の達人 : <b>雄叫び:</b> 次の自分のターンまで味方のミニオン1体に<b>隠れ身</b>を付与する。
		elif ID == 'NEW1_016':
			myCondition.append(['battlecry','', ''])
			#船長のオウム : [x]<b>雄叫び:</b>自分のデッキのランダムな海賊カード1枚を　自分の手札に追加する。
		elif ID == 'NEW1_017':
			myCondition.append(['battlecry','', ''])
			#飢えたカニ : <b>雄叫び:</b> マーロック1体を破壊し+2/+2を獲得する。
		elif ID == 'NEW1_018':
			myCondition.append(['battlecry','', ''])
			#ブラッドセイルの略奪者 : [x]<b>雄叫び:</b> 自分の武器の攻撃力に等しい攻撃力を　追加で獲得する。
		elif ID == 'NEW1_024':
			myCondition.append(['battlecry','', ''])
			#グリーンスキン船長 : [x]<b>雄叫び:</b>自分の武器に__+1/+1を付与する。
		elif ID == 'NEW1_025':
			myCondition.append(['battlecry','', ''])
			#ブラッドセイルの海賊 : [x]<b>雄叫び:</b> 敵の武器の耐久度を1減らす。
		elif ID == 'NEW1_029':
			myCondition.append(['battlecry','', ''])
			#ミルハウス・マナストーム : <b>雄叫び:</b>  次のターン敵の呪文のコストが（0）になる。
		elif ID == 'NEW1_030':
			myCondition.append(['battlecry','', ''])
			#デスウィング : [x]<b>雄叫び:</b> 自身を除く全てのミニオンを破壊し自分の手札を全て破棄する。
		elif ID == 'NEW1_041':
			myCondition.append(['battlecry','', ''])
			#暴走コドー : <b>雄叫び:</b> 攻撃力2以下の敵のミニオン1体をランダムに破壊する。
	elif 'OG_' in ID:
		if ID == 'OG_102':
			myCondition.append(['battlecry','', ''])
			#闇に説くもの : <b>雄叫び:</b> 味方のミニオン1体と攻撃力・体力を入れ替える。
		elif ID == 'OG_122':
			myCondition.append(['battlecry','', ''])
			#峡谷の暴君ムクラ : [x]<b>雄叫び:</b> 「バナナ」2枚を___自分の手札に追加する。
		elif ID == 'OG_131':
			myCondition.append(['battlecry','', ''])
			#双皇帝ヴェク＝ロア : [x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンの攻撃力が10以上ある場合もう1体の双皇帝を召喚する。
		elif ID == 'OG_133':
			myCondition.append(['battlecry','', ''])
			#頽廃させしものン＝ゾス : <b>雄叫び:</b> この対戦で死亡した味方の<b>断末魔</b>を持つミニオンを全て召喚する。
		elif ID == 'OG_134':
			myCondition.append(['battlecry','', ''])
			#希望の終焉ヨグ＝サロン : [x]<b>雄叫び:</b> この対戦で自分が使用した呪文1回につきランダムな呪文を1つ使用する<i>（対象は_____ランダムに選択される）。_</i>
		elif ID == 'OG_156':
			myCondition.append(['battlecry','', ''])
			#マーロックの鯛ド変態 : [x]<b>雄叫び:</b> <b>挑発</b>を持つ1/1のウーズを1体召喚する。
		elif ID == 'OG_161':
			myCondition.append(['battlecry','', ''])
			#コールドライトの妖幻者 : <b>雄叫び:</b> マーロックではない全てのミニオンに2ダメージを与える。
		elif ID == 'OG_162':
			myCondition.append(['battlecry','', ''])
			#クトゥーンの門弟 : <b>雄叫び:</b> 2ダメージを与える。自分のクトゥーンに+2/+2を付与する<i>（居場所は問わない）。</i>
		elif ID == 'OG_174':
			myCondition.append(['battlecry','', ''])
			#さまよう無貌のもの : [x]<b>挑発</b>、<b>雄叫び:</b>味方のミニオン1体の攻撃力と体力をコピーする。
		elif ID == 'OG_254':
			myCondition.append(['battlecry','', ''])
			#秘密を喰らうもの : [x]<b>雄叫び:</b> 敵の<b>秘策</b>全てを破壊する。破壊した秘策1つにつき+1/+1を獲得する。
		elif ID == 'OG_255':
			myCondition.append(['battlecry','', ''])
			#破滅の招き手 : <b>雄叫び:</b> 自分のクトゥーンに+2/+2を付与する<i>（居場所は問わない）。</i>クトゥーンが死亡している場合クトゥーン1枚を自分のデッキに混ぜる。
		elif ID == 'OG_280':
			myCondition.append(['battlecry','', ''])
			#クトゥーン : [x]<b>雄叫び:</b>このミニオンの攻撃力に等しい合計ダメージを敵に___ランダムに振り分ける。
		elif ID == 'OG_281':
			myCondition.append(['battlecry','', ''])
			#邪悪の誘い手 : [x]<b>雄叫び:</b>自分のクトゥーンに+2/+2を付与する<i>___（居場所は問わない）。</i>
		elif ID == 'OG_282':
			myCondition.append(['battlecry','', ''])
			#クトゥーンの刃 : [x]<b>雄叫び:</b>ミニオン1体を破壊する。その攻撃力と体力を自分のクトゥーンに追加する<i>（居場所は問わない）。</i>
		elif ID == 'OG_283':
			myCondition.append(['battlecry','', ''])
			#クトゥーンに選ばれし者 : [x]<b>聖なる盾</b>、<b>雄叫び:</b>自分のクトゥーンに+2/+2を付与する____<i>（居場所は問わない）。</i>
		elif ID == 'OG_284':
			myCondition.append(['battlecry','', ''])
			#黄昏の鎚の地霊術師 : [x]<b>挑発</b>、<b>雄叫び:</b>自分のクトゥーンに<b>挑発</b>を付与する____<i>（居場所は問わない）。</i>
		elif ID == 'OG_291':
			myCondition.append(['battlecry','', ''])
			#シャドーキャスター : [x]<b>雄叫び:</b>味方のミニオン1体を選択する。そのミニオンの1/1のコピーを自分の手札に追加する。_____そのカードのコストは（1）。_
		elif ID == 'OG_295':
			myCondition.append(['battlecry','', ''])
			#カルトの薬師 : <b>雄叫び:</b>敵のミニオン1体につき自分のヒーローの体力を#2回復する。
		elif ID == 'OG_320':
			myCondition.append(['battlecry','', ''])
			#ミッドナイト・ドレイク : <b>雄叫び:</b> このカード以外の自分の手札1枚につき攻撃力+1を獲得する。
		elif ID == 'OG_337':
			myCondition.append(['battlecry','', ''])
			#単眼の怪異 : [x]<b>挑発</b>、<b>雄叫び:</b> 敵のミニオン1体につき体力+1を獲得する。
		elif ID == 'OG_339':
			myCondition.append(['battlecry','', ''])
			#スケラムの狂信者 : [x]<b>雄叫び:</b> 自分のクトゥーンに+2/+2を付与する___<i>（居場所は問わない）。</i>_
	elif 'PRO_' in ID:
		if ID == 'PRO_001':
			myCondition.append(['battlecry','', ''])
			#エリート・トーレン・チーフテン : <b>雄叫び:</b>  両プレイヤーにロックなパワーあふれるカードを1枚ずつ与える。
	elif 'SCH_' in ID:
		if ID == 'SCH_160':
			myCondition.append(['battlecry','', ''])
			#ワンド職人 : [x]<b>雄叫び:</b>自分のクラスのコスト1の呪文1枚を____自分の手札に追加する。
		elif ID == 'SCH_162':
			myCondition.append(['battlecry','', ''])
			#ヴェクタス : [x]<b>雄叫び:</b>1/1のチビドラゴンを2体召喚する。それらはこの対戦で死亡した味方のミニオンの_____<b>断末魔</b>を1つずつ獲得する。
		elif ID == 'SCH_245':
			myCondition.append(['battlecry','', ''])
			#筆記の執精 : [x]<b>呪文ダメージ+1</b><b>雄叫び:</b>___呪文を1つ<b>発見</b>する。
		elif ID == 'SCH_248':
			myCondition.append(['battlecry','', ''])
			#ペン投げ野郎 : [x]<b>雄叫び:</b>1ダメージを与える。<b>魔法活性:</b>___これを自分の手札に戻す。
		elif ID == 'SCH_283':
			myCondition.append(['battlecry','', ''])
			#マナ食らいのパンサーラ : [x]<b>雄叫び:</b>このターンに自分がヒーローパワーを使っていた場合カードを1枚引く。
		elif ID == 'SCH_311':
			myCondition.append(['battlecry','', ''])
			#空飛ぶほうき : [x]<b>急襲</b>、<b>雄叫び:</b>自身を除く味方のミニオンに<b>急襲</b>を付与する。
		elif ID == 'SCH_312':
			myCondition.append(['battlecry','', ''])
			#ツアーガイド : <b>雄叫び:</b>自分が次に使うヒーローパワーのコストは（0）。
		elif ID == 'SCH_351':
			myCondition.append(['battlecry','', ''])
			#ジャンディス・バロフ : [x]<b>雄叫び:</b>ランダムなコスト5のミニオン2体を召喚する。2体の内、ダメージを受けると死ぬ1体を秘密裏に選ぶ。
		elif ID == 'SCH_428':
			myCondition.append(['battlecry','', ''])
			#伝承守護者ポルケルト : [x]<b>雄叫び:</b>自分のデッキのカードをコストが高い順に並べ替える。
		elif ID == 'SCH_522':
			myCondition.append(['battlecry','', ''])
			#スティールダンサー : [x]<b>雄叫び:</b>自分の武器の攻撃力に等しいコストのランダムなミニオンを1体召喚する。
		elif ID == 'SCH_530':
			myCondition.append(['battlecry','', ''])
			#代理鏡師 : [x]<b>雄叫び:</b>自分が<b>呪文ダメージ</b>を持っている場合このミニオンのコピーを1体召喚する。
		elif ID == 'SCH_713':
			myCondition.append(['battlecry','', ''])
			#教団の新入会員 : [x]<b>雄叫び:</b>次のターン、相手の呪文のコストが（1）増える。
	elif 'TRL_' in ID:
		if ID == 'TRL_071':
			myCondition.append(['battlecry','', ''])
			#ブラッドセイルの吠猿 : [x]<b>急襲</b>、<b>雄叫び:</b>自身を除く味方の海賊1体につき+1/+1を獲得する。
		elif ID == 'TRL_077':
			myCondition.append(['battlecry','', ''])
			#グルバシの盛り上げ屋 : [x]<b>雄叫び:</b><b>雄叫び</b>を持つミニオンの1/1のコピーを1体<b>発見</b>する。そのミニオンのコストは（1）になる。
		elif ID == 'TRL_096':
			myCondition.append(['battlecry','', ''])
			#グリフター : <b>雄叫び:</b>カードを2枚<b>発見</b>する。そのうちランダムな1枚を相手に与える。
		elif ID == 'TRL_126':
			myCondition.append(['battlecry','', ''])
			#フックタスク船長 : <b>雄叫び:</b>自分のデッキから海賊を3体召喚し_<b>急襲</b>を付与する。
		elif ID == 'TRL_151':
			myCondition.append(['battlecry','', ''])
			#元チャンピオン : [x]<b>雄叫び:</b>5/5の「期待の新人」を1体召喚する。
		elif ID == 'TRL_407':
			myCondition.append(['battlecry','', ''])
			#給水係 : [x]<b>雄叫び:</b>このターン中に自分が次に使用するヒーローパワーの_コストを（0）にする。
		elif ID == 'TRL_409':
			myCondition.append(['battlecry','', ''])
			#サメのロア・グラル : [x]<b>雄叫び:</b>_自分のデッキのミニオン1体を捕食してその攻撃力・体力を獲得する。<b>断末魔:</b>_そのミニオンを__自分の手札に追加する。
		elif ID == 'TRL_504':
			myCondition.append(['battlecry','', ''])
			#ブーティ・ベイのノミ屋 : [x]<b>雄叫び:</b>相手に「コイン」1枚を与える。
		elif ID == 'TRL_509':
			myCondition.append(['battlecry','', ''])
			#バナナ・バフーン : [x]<b>雄叫び:</b>「バナナ」2枚を___自分の手札に追加する。
		elif ID == 'TRL_512':
			myCondition.append(['battlecry','', ''])
			#小ずるい足噛み魔 : [x]<b>生命奪取</b>、<b>雄叫び:</b>__1ダメージを与える。
		elif ID == 'TRL_514':
			myCondition.append(['battlecry','', ''])
			#大虎ノーム : [x]<b>挑発</b>、<b>雄叫び:</b>相手の陣地にミニオンが2体以上いる場合______攻撃力+1を獲得する。
		elif ID == 'TRL_517':
			myCondition.append(['battlecry','', ''])
			#熱狂的闘技場ファン : <b>雄叫び:</b>自分の手札のミニオン全てに+1/+1を付与する。
		elif ID == 'TRL_523':
			myCondition.append(['battlecry','', ''])
			#ファイアーツリーの呪術医 : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合_____呪文を1つ<b>発見</b>する。
		elif ID == 'TRL_524':
			myCondition.append(['battlecry','heHasTaunt(game)', 'silence'])
			#シールドブレイカー : <b>雄叫び:</b><b>挑発</b>を持つ敵のミニオン1体を<b>沈黙</b>させる。
		elif ID == 'TRL_526':
			myCondition.append(['battlecry','', ''])
			#ドラゴンモーの爆炎竜 : [x]<b>雄叫び:</b>自身を除く全てのミニオンに______1ダメージを与える。
		elif ID == 'TRL_527':
			myCondition.append(['battlecry','', ''])
			#ドラッカリのトリックスター : <b>雄叫び:</b>各プレイヤーは相手のデッキからランダムなカードの__コピーを1枚得る。
		elif ID == 'TRL_530':
			myCondition.append(['battlecry','', ''])
			#覆面選手 : [x]<b>雄叫び:</b>自分の<b>秘策</b>が準備されている場合自分のデッキから___<b>秘策</b>を1つ準備する。
		elif ID == 'TRL_533':
			myCondition.append(['battlecry','', ''])
			#アイスクリーム屋 : [x]<b>雄叫び:</b>味方に<b>凍結中</b>のミニオンがいる場合_____装甲を8獲得する。
		elif ID == 'TRL_537':
			myCondition.append(['battlecry','', ''])
			#ダ・アンダテイカ : [x]<b>雄叫び:</b>この対戦で死亡した味方のミニオン3体の_____<b>断末魔</b>を獲得する。_
		elif ID == 'TRL_546':
			myCondition.append(['battlecry','', ''])
			#凶暴なリクガメ : [x]<b>雄叫び:</b>自分のヒーローに___5ダメージを与える。
		elif ID == 'TRL_564':
			myCondition.append(['battlecry','', ''])
			#モジョー使いジヒィ : <b>雄叫び:</b>各プレイヤーのマナクリスタルを5つにする。
		elif ID == 'TRL_569':
			myCondition.append(['battlecry','', ''])
			#ドッカンドラゴン : <b>雄叫び:</b>自分の手札にドラゴンがいる場合敵のミニオン1体に__7ダメージを与える。
	elif 'ULD_' in ID:
		if ID == 'ULD_003':
			myCondition.append(['battlecry','', ''])
			#偉大なるゼフリス : <b>雄叫び:</b>自分のデッキに重複するカードがない場合「勝利のカード」の願いを叶える。
		elif ID == 'ULD_157':
			myCondition.append(['battlecry','', ''])
			#クエスト中の探検家 : [x]<b>雄叫び:</b>自分が<b>クエスト</b>中の場合__カードを1枚引く。
		elif ID == 'ULD_178':
			myCondition.append(['battlecry','', ''])
			#シアマト : [x]<b>雄叫び:</b><b>急襲</b>、<b>挑発</b>、<b>聖なる盾</b><b>疾風</b>のうち、選択した___2つを獲得する。
		elif ID == 'ULD_186':
			myCondition.append(['battlecry','', ''])
			#ファラオの愛猫 : [x]<b>雄叫び:</b><b>蘇り</b>を持つランダムなミニオン1体を自分の__手札に追加する。
		elif ID == 'ULD_188':
			myCondition.append(['battlecry','', ''])
			#黄金スカラベ : <b>雄叫び:</b>コスト4のカード1枚を<b>発見</b>する。
		elif ID == 'ULD_189':
			myCondition.append(['battlecry','', ''])
			#無貌の潜むもの : [x]<b>挑発</b>、<b>雄叫び:</b>このミニオンの体力を2倍にする。
		elif ID == 'ULD_190':
			myCondition.append(['battlecry','', ''])
			#ピット・クロコリスク : <b>雄叫び:</b>5ダメージを与える。
		elif ID == 'ULD_191':
			myCondition.append(['battlecry','', ''])
			#笑顔の相棒 : [x]<b>雄叫び:</b>味方のミニオン1体に___体力+2を付与する。
		elif ID == 'ULD_196':
			myCondition.append(['battlecry','', ''])
			#ネフェルセトの儀式官 : <b>雄叫び:</b>隣接するミニオンの体力を上限まで回復する。
		elif ID == 'ULD_197':
			myCondition.append(['battlecry','', ''])
			#流砂のエレメンタル : [x]<b>雄叫び:</b>このターンの間敵のミニオン全てに____攻撃力-2を付与する。
		elif ID == 'ULD_209':
			myCondition.append(['battlecry','', ''])
			#ヴァルペラの悪党 : [x]<b>雄叫び:</b>呪文1つを<b>発見</b>するかミステリーチャンスに賭ける。
		elif ID == 'ULD_229':
			myCondition.append(['battlecry','', ''])
			#トラブルメーカー : [x]<b>雄叫び:</b>自分のデッキと相手のデッキの一番上の____カードを交換する。
		elif ID == 'ULD_271':
			myCondition.append(['battlecry','', ''])
			#傷を負ったトルヴィア : [x]<b>挑発</b>、<b>雄叫び:</b>このミニオンに____3ダメージを与える。
		elif ID == 'ULD_288':
			myCondition.append(['battlecry','', ''])
			#斂葬のアンカ : [x]<b>雄叫び:</b>自分の手札の<b>断末魔</b>を持つ各ミニオンをそれぞれコスト（1）の1/1に変える。
		elif ID == 'ULD_289':
			myCondition.append(['battlecry','', ''])
			#フィッシュフリンガー : [x]<b>雄叫び:</b>各プレイヤーの手札にランダムなマーロック1体を追加する。
		elif ID == 'ULD_304':
			myCondition.append(['battlecry','', ''])
			#ファオリス王 : [x]<b>雄叫び:</b>自分の手札の呪文1枚ごとに同コストのランダムな___ミニオンを1体召喚する。
		elif ID == 'ULD_327':
			myCondition.append(['battlecry','', ''])
			#バザール強盗 : [x]<b>急襲</b>、<b>雄叫び:</b>他のクラスのランダムなミニオン1体を自分の手札に追加する。
		elif ID == 'ULD_705':
			myCondition.append(['battlecry','', ''])
			#魔古の狂信者 : [x]<b>雄叫び:</b>自分の陣地が「魔古の狂信者」で一杯の場合それら全てを生贄にして「大番人ラー」を召喚する。
		elif ID == 'ULD_712':
			myCondition.append(['battlecry','', ''])
			#昆虫採集家 : <b>雄叫び:</b><b>急襲</b>を持つ1/1の「イナゴ」を1体召喚する。
		elif ID == 'ULD_719':
			myCondition.append(['battlecry','', ''])
			#サバクウサギ : <b>雄叫び:</b>1/1の「サバクウサギ」を2体召喚する。
		elif ID == 'ULD_727':
			myCondition.append(['battlecry','', ''])
			#包帯巻き職人 : [x]<b>雄叫び:</b>この対戦で死亡した味方のミニオンを1体<b>発見</b>し、それを自分のデッキに混ぜる。
	elif 'UNG_' in ID:
		if ID == 'UNG_001':
			myCondition.append(['battlecry','', ''])
			#プテロダックスのヒナ : <b>雄叫び:</b>___<b>適応</b>する。
		elif ID == 'UNG_002':
			myCondition.append(['battlecry','', ''])
			#ヴォルカノサウルス : <b>雄叫び:</b><b>適応</b>し、その後<b>適応</b>する。
		elif ID == 'UNG_009':
			myCondition.append(['battlecry','', ''])
			#ラヴァサウルスのチビ : <b>雄叫び:</b>このミニオンを除いて味方に2体以上のミニオンがいる場合<b>適応</b>する。
		elif ID == 'UNG_058':
			myCondition.append(['battlecry','', ''])
			#レイザーペタル・ラッシャー : [x]<b>雄叫び:</b>「レイザーペタル（1ダメージを与える）」1枚を自分の手札に追加する。
		elif ID == 'UNG_070':
			myCondition.append(['battlecry','', ''])
			#トルヴィアのストーンシェイパー : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合_______<b>挑発</b>と<b>聖なる盾</b>を獲得する。
		elif ID == 'UNG_072':
			myCondition.append(['battlecry','', ''])
			#ストーンヒルの守護者 : [x]<b>挑発</b>、<b>雄叫び:</b><b>挑発</b>を持つミニオン____1体を<b>発見</b>する。
		elif ID == 'UNG_073':
			myCondition.append(['battlecry','', ''])
			#ロックプール・ハンター : [x]<b>雄叫び:</b>味方のマーロック1体に+1/+1を付与する。
		elif ID == 'UNG_082':
			myCondition.append(['battlecry','', ''])
			#サンダーリザード : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合<b>適応</b>する。
		elif ID == 'UNG_084':
			myCondition.append(['battlecry','', ''])
			#ファイアプルーム・フェニックス : <b>雄叫び:</b>2ダメージを与える。
		elif ID == 'UNG_088':
			myCondition.append(['battlecry','', ''])
			#トートランの始原術師 : <b>雄叫び:</b>呪文1つを<b>発見</b>しランダムな対象に対して使用する。
		elif ID == 'UNG_089':
			myCondition.append(['battlecry','', ''])
			#温厚なメガサウルス : [x]<b>雄叫び:</b>味方のマーロック　全てを<b>適応</b>させる。
		elif ID == 'UNG_099':
			myCondition.append(['battlecry','', ''])
			#電撃デビルサウルス : [x]<b>突撃</b>、<b>雄叫び:</b>このターンの間ヒーローを攻撃できない。
		elif ID == 'UNG_113':
			myCondition.append(['battlecry','', ''])
			#輝く瞳の斥候 : <b>雄叫び:</b>カードを1枚引く。そのカードのコストを（5）に変える。
		elif ID == 'UNG_205':
			myCondition.append(['battlecry','heHasMinion()', 'damage'])
			#グレイシャル・シャード : <b>雄叫び:</b>敵1体を<b>凍結</b>させる。
		elif ID == 'UNG_801':
			myCondition.append(['battlecry','', ''])
			#巣作りロック鳥 : [x]<b>雄叫び:</b>このミニオンを除いて味方に2体以上のミニオンがいる場合<b>挑発</b>を獲得する。
		elif ID == 'UNG_803':
			myCondition.append(['battlecry','', ''])
			#エメラルド・リーヴァー : <b>雄叫び:</b>各ヒーローに1ダメージを与える。
		elif ID == 'UNG_807':
			myCondition.append(['battlecry','', ''])
			#ゴラッカ・クローラー : [x]<b>雄叫び:</b>海賊1体を破壊し__+1/+1を獲得する。
		elif ID == 'UNG_809':
			myCondition.append(['battlecry','', ''])
			#ファイアフライ : <b>雄叫び:</b>1/2のエレメンタル1体を自分の手札に追加する。
		elif ID == 'UNG_816':
			myCondition.append(['battlecry','', ''])
			#カリモスの下僕 : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合______エレメンタルを<b>発見</b>する。
		elif ID == 'UNG_840':
			myCondition.append(['battlecry','', ''])
			#ジャングルハンター・ヒーメット : [x]<b>雄叫び:</b>自分のデッキのコスト（3）以下の____カードを全て破壊する。
		elif ID == 'UNG_847':
			myCondition.append(['battlecry','', ''])
			#ブレイズコーラー : [x]<b>雄叫び:</b>前のターンに手札からエレメンタルを使用していた場合____5ダメージを与える。
		elif ID == 'UNG_848':
			myCondition.append(['battlecry','', ''])
			#始祖ドレイク : [x]<b>挑発</b>、<b>雄叫び:</b>自身を除く全てのミニオンに2ダメージを与える。
		elif ID == 'UNG_851':
			myCondition.append(['battlecry','', ''])
			#先遣隊長エリーズ : [x]<b>雄叫び:</b>自分のデッキに未開封の<b>ウンゴロ</b>パック1個を混ぜる。
		elif ID == 'UNG_907':
			myCondition.append(['battlecry','', ''])
			#オズラック : [x]<b>挑発</b>、<b>雄叫び:</b>前のターンに手札から使用したエレメンタル1体____につき体力+5を獲得する。
		elif ID == 'UNG_937':
			myCondition.append(['battlecry','', ''])
			#原始フィンの見張り番 : [x]<b>雄叫び:</b>自分の陣地に他のマーロックがいる場合マーロック1体を<b>発見</b>する。
		elif ID == 'UNG_946':
			myCondition.append(['battlecry','', ''])
			#暴蝕ウーズ : <b>雄叫び:</b>敵の武器を破壊しその攻撃力に等しい装甲を獲得する。
	elif 'YOD_' in ID:
		if ID == 'YOD_028':
			myCondition.append(['battlecry','', ''])
			#スカイダイビングの教官 : [x]<b>雄叫び:</b>自分のデッキからコスト1のミニオンを1体召喚する。
		elif ID == 'YOD_029':
			myCondition.append(['battlecry','', ''])
			#ヘイルブリンガー : <b>雄叫び:</b><b>凍結</b>を持つ1/1の「アイス・シャード」を2体召喚する。
		elif ID == 'YOD_030':
			myCondition.append(['battlecry','', ''])
			#認可冒険者 : [x]<b>雄叫び:</b>自分が<b>クエスト</b>中の場合自分の手札に「コイン」1枚を追加する。
		elif ID == 'YOD_033':
			myCondition.append(['battlecry','', ''])
			#ブームピストル無頼 : [x]<b>雄叫び:</b>次のターン敵の<b>雄叫び</b>を持つカードの__コストが（5）増える。
		elif ID == 'YOD_038':
			myCondition.append(['battlecry','', ''])
			#空賊大将クラッグ : [x]<b>挑発</b>、<b>雄叫び:</b>この対戦で<b>クエスト</b>を使用済みの場合<b>急襲</b>を持つ4/2のオウムを1体召喚する。
	return myCondition
