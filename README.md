# LOL Analysis
This repo includes a spider to crawl high elo(Challenger or Master) LOL games from [opgg](https://www.op.gg/), as well as some ML algorithm to provide game predictions based on team draft.

## Spider
Crawl the game data of summoners in [ranking ladder in opgg](https://www.op.gg/ranking/ladder/). For each game, record the team draft of two sides and the game result. Run `$python opgg.py [path]`, path is the file to store the crawled data. An example result is [*dataset/data/opgg.json*](https://raw.githubusercontent.com/Bowenduan/LOL_Analysis/master/data/dataset/opgg.json), which includes 60121 challengers' games. And the data is processed into [train(51121) and val(9000) data](https://github.com/Bowenduan/LOL_Analysis/tree/master/data/dataset).


## Model
All models are implemented [here](https://github.com/Bowenduan/LOL_Analysis/blob/master/train/model.py).<br>
Saved models are in [./model](https://github.com/Bowenduan/LOL_Analysis/tree/master/model).<br>
Current result:

| model | epoch | loss | acc | notes|
| ---   | ---   | ---  | --- | ---  |
|[fcnn](https://github.com/Bowenduan/LOL_Analysis/blob/master/train/train_fcnn.py)  |  80  | 0.4429| 87.02% | adam: lr=1e-3 epochs=40 -> lr=1e-4 epochs=40 |
|[fcnn+embedding](https://github.com/Bowenduan/LOL_Analysis/blob/master/train/train_fcnn_emb.py)| 80 | 0.4140 | 89.99% | adam lr=1e-3 epochs=40 -> lr=1e-4 epochs=40 |


:triangular_flag_on_post: TODO

* [x] split data into train and eval
* [x] add evaluation during training
* [x] saving model and lr schedular
* [x] fcnn+embedding code
* [x] fcnn lr schedular tune 
* [x] fcnn+embedding train
* [x] fcnn+embedding lr schedular tune 
* [ ] other models
