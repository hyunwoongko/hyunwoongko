# Resume
## 1. Biography
<details>
  <summary>
    <code>2014.03 ~ 2020.08</code>: BS in Software Engineering, Chonbuk National University
  </summary>

1. GPA
    - 4.15 (major) / 4.07 (minor)
    - 1st ranked.
2. Opensources
    - [Transformer](https://github.com/hyunwoongko/transformer): PyTorch implementation of Attention Is All You Need
    - [KoChat](https://github.com/hyunwoongko/kochat): The first Korean opensource chatbot framework
3. Awards
    - [2nd place in undergraduated student best paper awards held by Korea Information Technology Society](http://www.todayan.com/news/articleView.html?idxno=230207)
    - [3rd place in K-Hackerthon held by Korea MSIP (Ministry of Future, Planning and Science)](https://newsis.com/view/?id=NISX20181108_0000467462&cID=10808&pID=10800)
    - [5th place in Elecsthon held by KEPCO (Korea Electric Power Corporation)](https://blog.kepco.co.kr/1310)
4. ETC
    - I founded an [AI robot startup for autistic children](https://github.com/hyunwoongko/social-robot-bao).

</details>

<details>
  <summary>
    <code>2019.08 ~ 2020.08</code>: Undergraduate Researcher at Autonomous Robot Lab, Chonbuk National University
  </summary>

1. Researches
    - I conducted a research about [citrus pest and disease recognition](https://github.com/hyunwoongko/citrus-pest-disease-recognition).
    - I conducted a research about [autonomous strabismus recognition](https://github.com/hyunwoongko/strabismus-recognition).
2. ETC
    - I was a lecturer at [2020 Data Campus School](https://github.com/hyunwoongko/bigdata-lecture) held by Korea Data Agency.

</details>

<details>
  <summary>
    <code>2020.08 ~ 2021.02</code>: Machine Learning Engineer at <a href="https://kakaobrain.com">Kakao Brain</a>
  </summary>

1. [BrainQA](https://github.com/hyunwoongko/hyunwoongko/blob/main/assets/brainquiz.gif?raw=true)
    - I researched Korean quiz generation model.
    - This model was integrated to Pororo library (https://kakaobrain.github.io/pororo/seq2seq/qg.html)
2. [Pororo](https://github.com/kakaobrain/pororo)
    - Pororo is an opensource multilingual NLP toolkit.
    - I developed almost all generative models in Pororo such as Question Generation, Text Summarization and Machine Translation.
3. ETC
    - I hosted [Jiphyeonjeon](https://github.com/jiphyeonjeon), a natural language processing paper review group.

</details>

<details>
  <summary>
    <code>2021.03 ~ 2023.05</code>: Co-Founder & Machine Learning Engineer at <a href="https://tunib.ai">TUNiB</a>
  </summary>

1. [Coco & Mas](https://dearmate.ai/)
    - Coco & Mas are Korean persona chatbots which have dog persona.
    - We collected Korean chatbot dataset with crowdsourcers, and tested crowdsourcing methods to improve data quality and yield.
    - I pre-trained 1.3B Korean model to create these chatbots and fine-tune the models using the data we've collected.
    - I researched the impact of pre-training and continual learning techniques.
    - I deployed these models with Triton Inference Server and AWS ECS cluster.
2. [BLOONY](https://bloony.ai/)
    - BLOONY is an English chatbot powered by OpenAI GPT
    - I developed backend server using Java Spring Boot
    - I researched instruction following ability of OpenAI GPT3, and found innovate prompting methodology. In that time there's no instruction fine-tuned model, so the instruction following ability of the models was not very good. The methodology I made at the time became famous a year later as a technique called COT (Chain of thought).
    - I deployed overall services using AWS ECS cluster.
3. [TUNiBridge](https://tunibridge.ai/)
    - TUNiBridge is a service that provides various natural language models API.
    - I improved safety check module's TPS from 7 to 240 using NVIDIA TensorRT, Triton Inference Server and AWS ECS.
    - TUNiB N행시 service had been very popular in the Korean Internet community for about two weeks, with about 2 million requests per day. I improved the existing system to make the service more desirable.
    - I designed and developed overall system and deployed 20+ APIs.
4. Opensources
    - [OpenChat](https://github.com/hyunwoongko/openchat): Easy to use opensource chatting framework via neural networks
    - [Kss](https://github.com/hyunwoongko/kss): The most famous Korean sentence segmentation toolkit.
    - [Pecab](https://github.com/hyunwoongko/pecab): Pure python morpheme analyzer based on Mecab-ko-dic.
    - [Parallelformers](https://github.com/hyunwoongko/parallelformers): Easy-to-use transformer model deployment toolkit based on Hugging Face Transformers. The core mechanism of this library was integrated to Microsoft DeepSpeed Inference.
    - [Large-scale LM Tutorials](https://github.com/tunib-ai/large-scale-lm-tutorials): Large-scale language modeling tutorials with PyTorch
5. Awards
    - [1st place in Korea AI competetion held by Ministry of Science and ICT](https://m.etnews.com/20210715000270)
    - [1st place in Korean Document Abstractive Summarization Competition held by Dacon (username: gusdnd852)](https://dacon.io/competitions/open/235673/leaderboard)
6. ETC
    - I became a manager of [Chatbot Korea](https://facebook.com/groups/ChatbotDevKR), Korean facebook group for chatbot research.

</details>

<details>
  <summary>
    <code>2022.02 ~ 2023.09</code>: Lead Machine Learning Scientist at <a href="https://eleuther.ai">EleutherAI</a>
  </summary>
    
1. [Polyglot](https://github.com/EleutherAI/polyglot)
    - Polyglot is EleutherAI's multilingual modeling project.
    - We released 1B, 3B, 6B, 13B models trained on large-scale Korean dataset.
    - I was managing all members in Polyglot team and developing dataset preprocessing, training, evaluation pipelines.
2. [Japanese StableLM](https://stability.ai/blog/stability-ai-new-jplm-japanese-language-model-stablelm)
    - We released Japanese StableLM models by co-working StabilityAI Japan.
    - We released 7B foundation language model and instruction fine-tuned model.
3. [OSLO](https://github.com/EleutherAI/oslo)
    - OSLO is a framework that provides various GPU based optimization technologies for large-scale modeling.
    - Features like 3D parallelism and kernel fusion which could be useful when training a large model are the key features.
    - I was developing Tensor Parallelism, Pipeline Parallelism, Kernel Fusion, Activation Checkpointing engines.

</details>

<details>
  <summary>
    <code>2023.05 ~ present</code>: Machine Learning Researcher at <a href="https://kakaobrain.com">Kakao Brain</a>
  </summary>
    
1. Foundation Model Pre-training
    - I pre-trained KoGPT2, the foundation model at KakaoBrain.
    - Among its various sizes, the largest one is over 60B.
2. Long Context Fine-tuning
    - I conducted research to extend KoGPT2 for long contexts.
    - I tested various existing techniques and internal ideas.
    - I successfully extended the model from 4k length to 32k and 65k lengths.
3. Multimodal Fine-tuning
    - I conducted research on extending KoGPT2 for multimodal tasks, primarily text-image input and text output.
    - I combined vision encoders with auto-regressive language models, effectively handling image inputs.
4. Codebase Management
    - I am managing various internal codebases.
    - Notably, Megatron-LM for pre-training and OpenRLHF for alignment
5. ETC
    - I developed GKE (Google Kubernetes Engine) based evaluation pipelines.
    - I improved data deduplication pipeline, its speed has doubled by the improvement.
    - I improved monitoring / planning methods for language model pre-training.

</details>

## 2. Open Source Projects (100+ stars only)
- [Transformer, PyTorch implementation of Attention Is All You Need](https://github.com/hyunwoongko/transformer) (⭐2.0k+)
- [Pororo, Multilingual natural language processing toolkit](https://github.com/kakaobrain/pororo) (⭐1.2k+)
- [Parallelformers, Efficient model parallelization toolkit for deployment](https://github.com/tunib-ai/parallelformers) (⭐700+)
- [OpenChat, Easy to use opensource chatting framework via neural networks](https://github.com/hyunwoongko/openchat) (⭐400+)
- [KoChat, The first Korean opensource chatbot framework](https://github.com/hyunwoongko/kochat) (⭐400+)
- [Polyglot, Large language models of well-balanced competence in multi-languages](https://github.com/EleutherAI/polyglot) (⭐400+)
- [KSS, A Toolkit for Korean sentence segmentation](https://github.com/hyunwoongko/kss) (⭐300+)
- [OSLO, Open Source framework for Large-scale model Optimization](https://github.com/tunib-ai/oslo) (⭐300+)
- [Large-scale LM Tutorials, Large-scale language modeling tutorials with PyTorch](https://github.com/tunib-ai/large-scale-lm-tutorials) (⭐200+)
- [Pecab, Pure python Korean morpheme analyzer based on Mecab](https://githug.com/hyunwoongko/pecab) (⭐100+)

## 3. Awards
- [1st place in Korea AI competetion held by Ministry of Science and ICT](https://m.etnews.com/20210715000270)
- [1st place in Korean Document Abstractive Summarization Competition held by Dacon (username: gusdnd852)](https://dacon.io/competitions/open/235673/leaderboard)
- [2nd place in undergraduated student best paper awards held by Korea Information Technology Society](http://www.todayan.com/news/articleView.html?idxno=230207)
- [3rd place in K-Hackerthon held by Korea MSIP (Ministry of Future, Planning and Science)](https://newsis.com/view/?id=NISX20181108_0000467462&cID=10808&pID=10800)
- [5th place in Elecsthon held by KEPCO (Korea Electric Power Corporation)](https://blog.kepco.co.kr/1310)

## 4. Publications
- [A Technical Report for Polyglot-Ko: Open-Source Large-Scale Korean Language Models](https://arxiv.org/abs/2306.02254)

## 5. Contacts
- Github : [https://github.com/hyunwoongko](https://github.com/hyunwoongko)
- Twitter: [https://twitter.com/hyunwoongko](https://twitter.com/hyunwoongko)
- Facebook : [https://www.facebook.com/hyunwoongko](https://www.facebook.com/hyunwoongko)
- Instagram: [https://www.instagram.com/hyunwoong.ko](https://www.instagram.com/hyunwoong.ko)
- LinkedIn : [https://www.linkedin.com/in/hyunwoongko](https://www.linkedin.com/in/hyunwoongko)
