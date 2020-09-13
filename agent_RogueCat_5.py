def RogueCat_condition_poisonous(game,ID):
	myCondition=[]
	if ID  == 'BOT_565':
		myCondition.append(['poisonous','', ''])
		#ブライトノズル・クローラー : <b>断末魔:</b><b>猛毒</b>と<b>急襲</b>を持つ1/1のウーズを1体召喚する。
	elif ID  == 'BT_707':
		myCondition.append(['poisonous','', ''])
		#伏兵 : <b>秘策:</b>相手がミニオンを手札から使用した後<b>猛毒</b>を持つ2/3の伏兵を1体召喚する。
	elif ID  == 'DAL_077':
		myCondition.append(['poisonous','', ''])
		#毒々フィン : [x]<b>雄叫び:</b>味方のマーロック1体に<b>猛毒</b>を付与する。
	elif ID  == 'DRG_066':
		myCondition.append(['poisonous','', ''])
		#躱し身のキメラ : <b>猛毒</b>呪文とヒーローパワーの標的にならない。
	elif ID  == 'EX1_170':
		myCondition.append(['poisonous','', ''])
		#エンペラー・コブラ : <b>猛毒</b>
	elif ID  == 'EX1_191':
		myCondition.append(['poisonous','', ''])
		#病魔の運び手 : [x]<b>雄叫び:</b>味方のミニオン1体に<b>猛毒</b>を付与する。
	elif ID  == 'EX1_522':
		myCondition.append(['poisonous','', ''])
		#埋伏の暗殺者 : [x]<b>隠れ身</b>、<b>猛毒</b>
	elif ID  == 'FP1_010':
		myCondition.append(['poisonous','', ''])
		#マイエクスナ : <b>猛毒</b>
	elif ID  == 'GIL_683':
		myCondition.append(['poisonous','', ''])
		#沼地のドレイク : [x]<b>雄叫び:</b>相手の陣地に<b>猛毒</b>を持つ2/1の「ドレイクスレイヤー」を1体召喚する。
	elif ID  == 'ICC_032':
		myCondition.append(['poisonous','', ''])
		#毒術師 : <b>猛毒</b>
	elif ID  == 'ICC_809':
		myCondition.append(['poisonous','', ''])
		#疫病科学者 : [x]<b>コンボ:</b>味方のミニオン1体に<b>猛毒</b>を付与する。
	elif ID  == 'LOE_010':
		myCondition.append(['poisonous','', ''])
		#ピットスネーク : <b>猛毒</b>
	elif ID  == 'LOOT_125':
		myCondition.append(['poisonous','', ''])
		#石肌のバジリスク : <b>聖なる盾</b><b>猛毒</b>
	elif ID  == 'LOOT_315':
		myCondition.append(['poisonous','', ''])
		#トログのキノコ食い : [x]<b>挑発</b>、<b>猛毒</b>
	elif ID  == 'ULD_194':
		myCondition.append(['poisonous','', ''])
		#荒れ地のスコーピッド : <b>猛毒</b>
	elif ID  == 'ULD_715':
		myCondition.append(['poisonous','', ''])
		#狂気の災厄 : 各プレイヤーは<b>猛毒</b>を持つ2/2のナイフを装備する。
	elif ID  == 'UNG_808':
		myCondition.append(['poisonous','', ''])
		#不屈のカタツムリ : [x]<b>挑発</b>、<b>猛毒</b>
	elif ID  == 'UNG_814':
		myCondition.append(['poisonous','', ''])
		#巨大スズメバチ : [x]<b>隠れ身</b>、<b>猛毒</b>
	elif ID  == 'UNG_823':
		myCondition.append(['poisonous','', ''])
		#猛毒の仕込み : 自分の武器に<b>猛毒</b>を付与する。	
	return myCondition

def RogueCat_condition_rush(game,ID):
	myCondition=[]
	if ID  == 'BOT_020':
		myCondition.append(['rush','', ''])
		#スケボーロボ : <b>超電磁</b><b>急襲</b>
	elif ID  == 'BOT_102':
		myCondition.append(['rush','', ''])
		#スパーク・ドリル : [x]<b>急襲</b><b>断末魔:</b><b>急襲</b>を持つ1/1の「スパーク」2体を自分の手札に追加する。
	elif ID  == 'BOT_538':
		myCondition.append(['rush','', ''])
		#スパーク・エンジン : [x]<b>雄叫び:</b><b>急襲</b>を持つ1/1の「スパーク」1体を____自分の手札に追加する。
	elif ID  == 'BOT_548':
		myCondition.append(['rush','', ''])
		#ジリアックス : <b>超電磁</b><b>聖なる盾</b>、<b>挑発</b><b>生命奪取</b>、<b>急襲</b>
	elif ID  == 'BOT_565':
		myCondition.append(['rush','', ''])
		#ブライトノズル・クローラー : <b>断末魔:</b><b>猛毒</b>と<b>急襲</b>を持つ1/1のウーズを1体召喚する。
	elif ID  == 'BOT_603':
		myCondition.append(['rush','', ''])
		#スティール・レイジャー : <b>急襲</b>
	elif ID  == 'BT_156':
		myCondition.append(['rush','', ''])
		#封印されしヴァイルフィーンド : [x]2ターンの間、<b>休眠状態</b>。<b>急襲</b>
	elif ID  == 'BT_720':
		myCondition.append(['rush','', ''])
		#錆鉄騎の略奪者 : <b>挑発</b>、<b>急襲</b><b>雄叫び:</b>このターンの間__攻撃力+4を獲得する。
	elif ID  == 'BT_723':
		myCondition.append(['rush','', ''])
		#ロケット改造屋 : [x]<b>雄叫び:</b>ミニオン1体に1ダメージを与え_____<b>急襲</b>を付与する。_
	elif ID  == 'DAL_565':
		myCondition.append(['rush','', ''])
		#ポータル・オーバーフィーンド : <b>雄叫び:</b>自分のデッキにポータル3枚を混ぜる。それを引いた際<b>急襲</b>を持つ2/2の悪魔を1体召喚する。
	elif ID  == 'DAL_582':
		myCondition.append(['rush','', ''])
		#ポータルの番人 : <b>雄叫び:</b>自分のデッキにポータル3枚を混ぜる。それを引いた際<b>急襲</b>を持つ2/2の悪魔を1体召喚する。
	elif ID  == 'DAL_592':
		myCondition.append(['rush','', ''])
		#石頭 : [x]<b>急襲</b>このミニオンの攻撃でミニオンが死亡した後__再度攻撃できる。
	elif ID  == 'DAL_714':
		myCondition.append(['rush','', ''])
		#最下層の故買屋 : [x]<b>雄叫び:</b>自分の手札に他のクラスのカードがある場合+1/+1と<b>急襲</b>を獲得する。
	elif ID  == 'DAL_743':
		myCondition.append(['rush','', ''])
		#ヘンチ・クランの騎豚 : [x]<b>急襲</b>、<b>断末魔:</b>1/1のマーロックを1体召喚する。
	elif ID  == 'DAL_760':
		myCondition.append(['rush','', ''])
		#バーリー・ショベルフィスト : <b>急襲</b>
	elif ID  == 'DAL_773':
		myCondition.append(['rush','', ''])
		#魔法の絨毯 : [x]自分がコスト1のミニオンを手札から使用した後そのミニオンに攻撃力+1と<b>急襲</b>を付与する。
	elif ID  == 'DRG_050':
		myCondition.append(['rush','', ''])
		#心血注ぐ献身者 : <b>急襲</b>、<b>雄叫び:</b>ガラクロンドに<b>祈願</b>する。
	elif ID  == 'DRG_059':
		myCondition.append(['rush','', ''])
		#ゴボグライダー技士 : [x]<b>雄叫び:</b>自分の陣地にメカがいる場合+1/+1と<b>急襲</b>を獲得する。
	elif ID  == 'DRG_061':
		myCondition.append(['rush','', ''])
		#オートジャイロ : <b>急襲</b>、<b>疾風</b>
	elif ID  == 'DRG_063':
		myCondition.append(['rush','', ''])
		#ドラゴンモーの密猟者 : <b>雄叫び:</b>相手の陣地にドラゴンがいる場合、+4/+4と<b>急襲</b>を獲得する。
	elif ID  == 'DRG_065':
		myCondition.append(['rush','', ''])
		#ヒポグリフ : <b>急襲</b>、<b>挑発</b>
	elif ID  == 'DRG_076':
		myCondition.append(['rush','', ''])
		#無貌の変性者 : <b>急襲</b>、<b>雄叫び:</b>味方のミニオン1体をこのミニオンのコピーに変身させる。
	elif ID  == 'DRG_079':
		myCondition.append(['rush','', ''])
		#躱し身のワーム : <b>聖なる盾</b>、<b>急襲</b>呪文とヒーローパワーの標的にならない。
	elif ID  == 'GIL_143':
		myCondition.append(['rush','', ''])
		#獰猛なスケイルハイド : <b>生命奪取</b>、<b>急襲</b>
	elif ID  == 'GIL_202':
		myCondition.append(['rush','', ''])
		#ギルニーアスの近衛兵 : [x]<b>聖なる盾</b>、<b>急襲</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。
	elif ID  == 'GIL_528':
		myCondition.append(['rush','', ''])
		#俊足な使者 : [x]<b>急襲</b>このカードが自分の手札にある場合、毎ターンこれの攻撃力と体力を入れ替える。
	elif ID  == 'GIL_557':
		myCondition.append(['rush','', ''])
		#呪われた漂流者 : [x]<b>急襲</b>、<b>断末魔:</b>自分のデッキから<b>コンボ</b>カードを_1枚引く。
	elif ID  == 'GIL_578':
		myCondition.append(['rush','', ''])
		#アッシュモア伯爵夫人 : [x]<b>雄叫び:</b>自分のデッキから<b>急襲</b><b>生命奪取</b>、<b>断末魔</b>を持つカードをそれぞれ1枚引く。
	elif ID  == 'GIL_601':
		myCondition.append(['rush','', ''])
		#スケイルワーム : [x]<b>雄叫び:</b>自分の手札にドラゴンがいる場合攻撃力+1と<b>急襲</b>を獲得する。
	elif ID  == 'GIL_682':
		myCondition.append(['rush','', ''])
		#マックハンター : [x]<b>急襲</b>、<b>雄叫び:</b>相手の陣地に2/1の「マックリング」_を2体召喚する。
	elif ID  == 'SCH_182':
		myCondition.append(['rush','', ''])
		#自然の語り手ギドラ : [x]<b>急襲</b>、<b>疾風</b><b>魔法活性:</b>使われた呪文のコストに等しい攻撃力と体力を獲得する。
	elif ID  == 'SCH_311':
		myCondition.append(['rush','', ''])
		#空飛ぶほうき : [x]<b>急襲</b>、<b>雄叫び:</b>自身を除く味方のミニオンに<b>急襲</b>を付与する。
	elif ID  == 'SCH_425':
		myCondition.append(['rush','', ''])
		#ドクター・クラスティノフ : [x]<b>急襲</b>このミニオンが攻撃する度自分の武器に+1/+1を付与する。
	elif ID  == 'SCH_707':
		myCondition.append(['rush','', ''])
		#空を翔けるトビウオ : [x]<b>急襲</b>、<b>断末魔:</b><b>急襲</b>を持つ4/3の幽霊1体を自分の___手札に追加する。
	elif ID  == 'TRL_020':
		myCondition.append(['rush','', ''])
		#盲目のレンジャー : [x]<b>急襲</b>、<b>血祭:</b>1/1の「コウモリ」を2体召喚する。
	elif ID  == 'TRL_071':
		myCondition.append(['rush','', ''])
		#ブラッドセイルの吠猿 : [x]<b>急襲</b>、<b>雄叫び:</b>自身を除く味方の海賊1体につき+1/+1を獲得する。
	elif ID  == 'TRL_074':
		myCondition.append(['rush','', ''])
		#ギザギザの歯 : [x]<b>断末魔:</b>味方のミニオン全てに<b>急襲</b>を付与する。
	elif ID  == 'TRL_126':
		myCondition.append(['rush','', ''])
		#フックタスク船長 : <b>雄叫び:</b>自分のデッキから海賊を3体召喚し_<b>急襲</b>を付与する。
	elif ID  == 'TRL_542':
		myCondition.append(['rush','', ''])
		#ウーンダスタ : [x]<b>急襲</b>、<b>血祭:</b>自分の手札から____獣を1体召喚する。
	elif ID  == 'TRL_550':
		myCondition.append(['rush','', ''])
		#アマニの戦熊 : <b>急襲</b>、<b>挑発</b>
	elif ID  == 'ULD_178':
		myCondition.append(['rush','', ''])
		#シアマト : [x]<b>雄叫び:</b><b>急襲</b>、<b>挑発</b>、<b>聖なる盾</b><b>疾風</b>のうち、選択した___2つを獲得する。
	elif ID  == 'ULD_327':
		myCondition.append(['rush','', ''])
		#バザール強盗 : [x]<b>急襲</b>、<b>雄叫び:</b>他のクラスのランダムなミニオン1体を自分の手札に追加する。
	elif ID  == 'ULD_712':
		myCondition.append(['rush','', ''])
		#昆虫採集家 : <b>雄叫び:</b><b>急襲</b>を持つ1/1の「イナゴ」を1体召喚する。
	elif ID  == 'YOD_038':
		myCondition.append(['rush','', ''])
		#空賊大将クラッグ : [x]<b>挑発</b>、<b>雄叫び:</b>この対戦で<b>クエスト</b>を使用済みの場合<b>急襲</b>を持つ4/2のオウムを1体召喚する。
	return myCondition



