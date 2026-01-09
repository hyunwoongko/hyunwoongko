# Curriculum Vitae
## 1. Who am I?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/hyunwoongko/hyunwoongko/assets/38183241/1fdac571-2e3e-497a-babc-31609f98094a" width=50%>

- Name: Hyunwoong Ko (Kevin Ko)
- Birth: 1995.09.12
- Job: Software Engineer / AI Researcher

## 2. Skill Sets
- Languages
  - Python: Excellent
  - Java: Excellent
  - C++: Available
- Topics
  - Language model pre-training
  - Language model alignment
  - Language model optimization
  - Multimodal model training
  - Prompt programming
  - Korean language processing
  - Data processing and crawling
  - Distributed programming
  - DevOps / MLOps
  - Backend development
- Libraries
  - Language model training: Pytorch, Transformers, Megatron-LM, DeepSpeed, TRL and OpenRLHF
  - Language model evaluation: LM-evaluation-harness
  - Language model optimization: Torchscript, Triton inference server, ONNX and TensorRT, VLLM, Flash Attention
  - DevOps: Docker, Kubernetes, ECS, EKS, GKE, Github Action and Code Pipeline
  - Backend development: Flask, FastAPI and Spring Boot

## 3. Biography
#### [<code>2014.03 ~ 2020.08</code>] BS in Software Engineering, Chonbuk National University
1. GPA
    - 4.15 (major) / 4.07 (total)
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

#### [<code>2019.08 ~ 2020.08</code>] Undergraduate Researcher at Autonomous Robot Lab, Chonbuk National University
1. Researches
    - I conducted a research about [citrus pest and disease recognition](https://github.com/hyunwoongko/citrus-pest-disease-recognition).
    - I conducted a research about [autonomous strabismus recognition](https://github.com/hyunwoongko/strabismus-recognition).
2. ETC
    - I was a lecturer at [2020 Data Campus School](https://github.com/hyunwoongko/bigdata-lecture) held by Korea Data Agency.

#### [<code>2020.08 ~ 2021.02</code>] Machine Learning Engineer at <a href="https://kakaobrain.com">Kakao Brain</a>
1. [BrainQA](https://github.com/hyunwoongko/hyunwoongko/blob/main/assets/brainquiz.gif)
    - I researched Korean quiz generation model.
    - This model was integrated to [Pororo library](https://kakaobrain.github.io/pororo/seq2seq/qg.html)
2. [Pororo](https://github.com/kakaobrain/pororo)
    - Pororo is an opensource multilingual NLP toolkit.
    - I developed almost all generative models in Pororo such as Question Generation, Text Summarization and Machine Translation.
3. ETC
    - I hosted [Jiphyeonjeon](https://github.com/jiphyeonjeon), a natural language processing paper review group.
 
#### [<code>2021.03 ~ 2023.05</code>] Co-Founder & Machine Learning Engineer at <a href="https://tunib.ai">TUNiB</a>
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
    - [Large-scale LM Tutorials](https://github.com/tunib-ai/large-scale-lm-tutorials): Large-scale language modeling tutorials with PyTorch
    - [Parallelformers](https://github.com/hyunwoongko/parallelformers): Easy-to-use transformer model deployment toolkit based on Hugging Face Transformers. The core mechanism of this library was integrated to Microsoft DeepSpeed Inference.
5. Awards
    - [1st place in Korea AI competetion held by Ministry of Science and ICT](https://m.etnews.com/20210715000270)
    - [1st place in Korean Document Abstractive Summarization Competition held by Dacon (username: gusdnd852)](https://dacon.io/competitions/open/235673/leaderboard)
6. ETC
    - I became a manager of [Chatbot Korea](https://facebook.com/groups/ChatbotDevKR), Korean facebook group for chatbot research.
 
#### [<code>2022.02 ~ 2023.09</code>] Lead Machine Learning Scientist at <a href="https://eleuther.ai">EleutherAI</a>
1. [Polyglot](https://github.com/EleutherAI/polyglot)
    - Polyglot is EleutherAI's multilingual modeling project.
    - We collected 1.2 TB of korean texts for language model pre-training.
    - We released 1B, 3B, 6B, 13B models trained on large-scale Korean dataset.
    - We publihed [a technical report of polyglot-ko](https://arxiv.org/abs/2306.02254)
    - I was managing all members in Polyglot team and developing dataset preprocessing, training, evaluation pipelines.
2. [Japanese StableLM](https://stability.ai/blog/stability-ai-new-jplm-japanese-language-model-stablelm)
    - We released Japanese StableLM models by co-working StabilityAI Japan.
    - We released 7B foundation language model and instruction fine-tuned model.
3. [OSLO](https://github.com/EleutherAI/oslo)
    - OSLO is a framework that provides various GPU based optimization technologies for large-scale modeling.
    - Features like 3D parallelism and kernel fusion which could be useful when training a large model are the key features.
    - I was developing Tensor Parallelism, Pipeline Parallelism, Kernel Fusion, Activation Checkpointing engines.
 
#### [<code>2023.05 ~ 2024.06</code>] Machine Learning Researcher at <a href="https://kakaobrain.com">Kakao Brain</a>
1. Foundation Model Pre-training
    - I pre-trained KoGPT2, the foundation model at KakaoBrain.
    - Among its various sizes, the largest one is over 60B.
    - It got similar performance with LLaMA2 in English, much better in Korean.
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
5. Publication
    - [ACL 2024 accepted] [Length-aware Byte Pair Encoding for Mitigating Over-segmentation in Korean Machine Translation](https://aclanthology.org/2024.findings-acl.135/)
6. ETC
    - I developed GKE (Google Kubernetes Engine) based evaluation pipelines.
    - I improved data deduplication pipeline, its speed has doubled by the improvement.
    - I improved monitoring / planning methods for language model pre-training.

#### [<code>2024.06 ~ present</code>] Machine Learning Researcher at <a href="https://kakaocorp.com">Kakao</a>
1. Language Model Alignment
    - I trained Kanana `1.0`, `1.5`, `1.5-thinking (internal)` and `2.0-instruct` models.
      - [kanana-nano-2.1b-instruct](https://huggingface.co/kakaocorp/kanana-nano-2.1b-instruct) (sft project leader)
      - [kanana-1.5-8b-instruct-2505](https://huggingface.co/kakaocorp/kanana-1.5-8b-instruct-2505) (sft project leader)
      - [kanana-1.5-15.7b-a3b-instruct](https://huggingface.co/kakaocorp/kanana-1.5-15.7b-a3b-instruct) (on-policy distillation)
      - [kanana-2-30b-a3b-instruct](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct) (instruct project leader)
      - Especially, Kanana-2-30b-a3b-instruct model got similar performance with Qwen3-30b-a3b model. 
    - I wrote multiple technical blogs.
      - [국내 최초 MoE 모델 ‘Kanana-MoE’ 개발기](https://tech.kakao.com/posts/716)
      - [Kanana 언어모델에 추론 기능 붙여보기 (feat. Kanana-1.5)](https://tech.kakao.com/posts/724)
    - I developed an interenal evaluation framework for aligned models.
2. Multimodal Foundation Model
    - I trained [kanana-1.5-v-3b-instruct](https://huggingface.co/kakaocorp/kanana-1.5-v-3b-instruct).
    - Especially, I developed preference learning (DPO) feature in our internal codebase and focused on DPO training.
3. Publication
    - [Kanana: Compute-efficient Bilingual Language Models](https://arxiv.org/abs/2502.18934)
4. Opensources
    - [nanoRLHF](https://github.com/hyunwoongko/nanoRLHF): from-scratch implementation of apache arrow, ray, megatron-lm, vllm, verl and flash attention
## 4. How to contact?
- Github : [https://github.com/hyunwoongko](https://github.com/hyunwoongko)
- Twitter: [https://twitter.com/hyunwoongko](https://twitter.com/hyunwoongko)
- Facebook : [https://www.facebook.com/hyunwoongko](https://www.facebook.com/hyunwoongko)
- Instagram: [https://www.instagram.com/hyunwoong.ko](https://www.instagram.com/hyunwoong.ko)
- LinkedIn : [https://www.linkedin.com/in/hyunwoongko](https://www.linkedin.com/in/hyunwoongko)
