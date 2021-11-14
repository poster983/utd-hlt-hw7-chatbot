# utd-hlt-hw7-chatbot
Tom Riddle Chatbot

## To run
```shell
> flask run 
```

## To Install
```shell 
> python3 -m venv .venv
> source ./.venv/bin/activate
> pip3 install -r requirements.txt
```

### Note for M1 Macs  
[See This](https://github.com/explosion/spaCy/issues/7962)

1. ```shell 
    > brew install openblas
    ```
2. ```shell
    > python3.9 -m venv .venv
    > source myvenv/bin/activate
    > python -m pip install -U pip setuptools wheel
    ```
3. Create a file called constraints.txt that specifies an older version of numpy without the wheel problem for use in isolated builds:
```
numpy==1.19.2
spacy==2.1.9
```
(Should be done in this repo already)

4. Run this:  
```shell
> PIP_CONSTRAINT=constraints.txt OPENBLAS="$(brew --prefix openblas)" pip install spacy
```  
```shell
> PIP_CONSTRAINT=constraints.txt OPENBLAS="$(brew --prefix openblas)" pip install chatterbot
```

5. 
```shell 
> pip3 install -r requirements.txt
```