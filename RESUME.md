# Curriculum Vitae

<p align="center">
  <img src="https://github.com/hyunwoongko/hyunwoongko/assets/38183241/1fdac571-2e3e-497a-babc-31609f98094a" width=50%>  
</p>

- Name: Hyunwoong Ko (Kevin Ko)
- Birth: 1995.09.12
- Job: Software Engineer / AI Researcher
- Social Media: [Github](https://github.com/hyunwoongko), [Facebook](https://www.facebook.com/hyunwoongko), [LinkedIn](https://www.linkedin.com/in/hyunwoongko)

## Skills
- Languages
  - Python (Excellent), Java (Excellent), C++ (Available)
- Topics
  - LLM Pre-training, LLM Alignment, LLM Optimization, DevOps, Backend Development
- Tools
  - Training: PyTorch, Transformers, Megatron-LM, DeepSpeed, Verl, Nemo-RL
  - Evaluation: LM-Evaluation-Harness, Nemo-Evaluator
  - Optimization: Triton, ONNX, TensorRT, vLLM, Flash Attention
  - DevOps: Docker, Kubernates, ECS, EKS, GKE, Github Action
  - Backend Dev: FastAPI, Flask, Spring Boot

## Work Experiences
### Kakao Corp (LLM Researcher): 2024.06 ~ present
- Language Model Alignment (Part Leader)
  - SFT: [Kanana-nano-2.1b-instruct](https://huggingface.co/kakaocorp/kanana-nano-2.1b-instruct)
  - SFT: [Kanana-1.5-8b-instruct-2505](https://huggingface.co/kakaocorp/kanana-1.5-8b-instruct-2505)
  - GKD: [Kanana-1.5-15.7b-a3b-instruct](https://huggingface.co/kakaocorp/kanana-1.5-15.7b-a3b-instruct)
  - SFT & RL: [Kanana-2-30b-a3b-instruct](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct)
    - Kanana-2-30b-a3b-instruct got similar performance with Qwen3-30B-A3B
  - Developed internal evaluation framework (OpenEval)
  - Developed internal training framework (OpenRLHF & Verl)
- Multi-modal Foundation Model (Team Member)
  - DPO: [Kanana-1.5-v-3b-instruct](https://huggingface.co/kakaocorp/kanana-1.5-v-3b-instruct)

### Kakao Brain (LLM Researcher): 2023.05 ~ 2024.05
- Language Model Pre-training (Team Member)
  - Pre-training: KoGPT2-66B
    - KoGPT2-66B got similar performance with LLaMA2-70B
  - Long-context Fine-tuning (4k to 32k)
  - Developed inteneral training framework (Megatron-LM)

### EleutherAI (ML Scientist): 2022.02 ~ 2023.09
- Language Model Pre-training (Team Leader)
  - Pre-training: [Polyglot-Ko](https://github.com/EleutherAI/polyglot)
    - Polyglot-Ko is the first commercially usable open source Korean LLM
  - Data processing: [Japanese StableLM](https://stability.ai/blog/stability-ai-new-jplm-japanese-language-model-stablelm)
- Framework Development (Team Leader)
  - Developed TP, PP, Kernel Fusion: [OSLO](https://github.com/EleutherAI/oslo)

### TUNiB (Co-Founder): 2021.03 ~ 2023.05
- Chatbot Research (Team Leader)
  - CPT & SFT: [Coco & Mas](https://dearmate.ai/)
  - Prompt Engineering & Backend Dev: [BLOONY](https://www.youtube.com/watch?v=5UfC2H19r6c)
- API Serving (Team Leader)
  - Model Optimization using ONNX & TensorRT
  - Serve API Servers using AWS ECS & Triton Inference Server

### Kakao Brain (ML Enginer): 2020.08 ~ 2021.02
- Framework Development
  - Question Generation, Text Summarization, Machine Translation: [Pororo](https://github.com/kakaobrain/pororo)

### Chonbuk National University (Undergrad Researcher): 2019.08 ~ 2020.08
- Research: [Citrus Pest and Disease Recognition](https://github.com/hyunwoongko/citrus-pest-disease-recognition)
- Research: [Autonomous Strabismus Recognition](https://github.com/hyunwoongko/strabismus-recognition)

## Open Sources
- [nanoRLHF](https://github.com/hyunwoongko/nanoRLHF): From-scratch Implementation of Arrow, Ray, Megatron-LM, Flash attention, vLLM and Verl
- [OSLO](https://github.com/tunib-ai/oslo): Open Source Framework for Large-scale Model Optimization
- [Parallelformers](https://github.com/hyunwoongko/parallelformers): LLM Deployment Toolkit based on HF Transformers. (integrated to DeepSpeed Inference)
- [Large-scale LM Tutorials](https://github.com/tunib-ai/large-scale-lm-tutorials): Large-scale Language Modeling Tutorials with PyTorch
- [Kss](https://github.com/hyunwoongko/kss): The Most Famous Korean Sentence Segmentation Toolkit.
- [Pecab](https://github.com/hyunwoongko/pecab): Pure Python Morpheme Analyzer based on Mecab-ko-dic.
- [KoChat](https://github.com/hyunwoongko/kochat): The First Korean Open Source Chatbot Framework
- [OpenChat](https://github.com/hyunwoongko/openchat): Easy to use Opensource Chatbot Framework via Neural Networks
- [Pororo](https://github.com/kakaobrain/pororo): Open Source Multilingual NLP toolkit. (Github 1k+ stars)
- [Transformer](https://github.com/hyunwoongko/transformer): PyTorch Implementation of Attention Is All You Need (Github 4k+ stars)

## Education
- BS in Software Engineering, Chonbuk National University
  - GPA: 4.15 (major) / 4.07 (total), 1st ranked

## Publications
- [Kanana: Compute-efficient Bilingual Language Models](https://arxiv.org/abs/2502.18934) (arXiv preprint)
- [Length-aware Byte Pair Encoding for Mitigating Over-segmentation in Korean Machine Translation](https://aclanthology.org/2024.findings-acl.135/) (ACL 2024 Findings)
- [A Technical Report for Polyglot-Ko: Open-Source Large-Scale Korean Language Models](https://arxiv.org/abs/2306.02254) (arXiv preprint)

## Activities
- Blog writing: [Kanana 언어모델에 추론 기능 붙여보기 (feat. Kanana-1.5)](https://tech.kakao.com/posts/724)
- Blog writing: [국내 최초 MoE 모델 ‘Kanana-MoE’ 개발기](https://tech.kakao.com/posts/716)
- Presentation (챗GPT 러닝데이): [딥러닝 병렬처리 및 Polyglot 언어모델](https://www.youtube.com/watch?v=a0TB-_WFjNk)
- Presentation (LangCon 2023): [EleutherAI에서의 1년](https://www.youtube.com/watch?v=yeAY_7cQj5k)
- Presentation (LangCon 2021): [Parallelformers: 빅모델 배포를 향한 여정](https://www.youtube.com/watch?v=eHqUMThhs2A)
- Presentation (집현전): [Large-scale LM에 대한 얕고 넓은 지식들](https://www.youtube.com/watch?v=w4a-ARCEiqU)
- Presentation (AI Star): [새로운 AI 챗봇?! 오픈소스 AI와 지금 직접 채팅을 해보세요.](https://www.youtube.com/watch?v=uN-OBI0n0JE)
- Lecturer: [2020 Data Campus School](https://github.com/hyunwoongko/bigdata-lecture)
- Manager: [Chatbot Korea](https://facebook.com/groups/ChatbotDevKR), Korean Facebook Group for Chatbot
- Manager: [Jiphyeonjeon](https://github.com/jiphyeonjeon), NLP Paper Review Group

## Awards
- [1st place in Korean Document Abstractive Summarization Competition held by Dacon](https://dacon.io/competitions/open/235673/leaderboard) (username: gusdnd852)
- [1st place in Korea AI competetion held by Ministry of Science and ICT](https://m.etnews.com/20210715000270)
- [2nd place in undergraduated student best paper awards held by Korea Information Technology Society](http://www.todayan.com/news/articleView.html?idxno=230207)
- [3rd place in K-Hackerthon held by Korea MSIP (Ministry of Future, Planning and Science)](https://newsis.com/view/?id=NISX20181108_0000467462&cID=10808&pID=10800)
