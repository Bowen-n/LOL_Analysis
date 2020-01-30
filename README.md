# LOL_Analysis
This repo includes a spider to crawl high elo(Challenger or Master) LOL games from [opgg](https://www.op.gg/), as well as some ML algorithm to provide game predictions based on team draft.

## Spider
Crawl the game data of summoners in [ranking ladder in opgg](https://www.op.gg/ranking/ladder/). For each game, record the team draft of two sides and the game result. Run `$python opgg.py [path]`, path is the file to store the crawled data. An example result is */dataset/data/opgg.json*.


## Predictor
:triangular_flag_on_post: TODO