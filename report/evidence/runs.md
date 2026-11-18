# Результаты запусков 17 ноября 2026 года

Все перечисленные запуски выполнены планировщиком Hermes на VPS. Первые семь значений времени взяты из журнала cron, последние два — из измерений Python-сценария. Ожидание расписания в них не входит. Для первых семи задан период поиска 365 суток, для последних двух — 7 суток.

| Начало, МСК, 17 ноября | Модель | Время, с | Входные / выходные токены | Результат |
|---|---|---:|---:|---|
| 03:05 по расписанию | Nemotron 3.5 Lightning free | 54,087 | 453 632 / 876 | Неверный синтаксис запроса, отправка подавлена |
| 03:10 по расписанию | Та же | 5,284 | 35 737 / 690 | Посторонние статьи, отправка подавлена |
| 03:15 по расписанию | Та же | 114,941 | 186 654 / 1 493 | Остановка по лимиту шагов |
| 11:26:57 фактически | Nemotron 3 Ultra free | 13,980 | 17 949 / 1 026 | Доставлено; в подборке есть смешанная реальность |
| 11:32:57 фактически | Та же | 8,906 | 17 291 / 767 | Подборка доставлена |
| 11:38:57 фактически | Та же | 4,051 | 17 947 / 147 | Ответ [SILENT], отправка подавлена |
| 22:39:57 фактически | Та же | 32,089 | 17 378 / 1 187 | Доставлено шесть статей вместо заданных трёх |
| 23:10:14 фактически | Nemotron 3 Ultra free | 9,116 | 904 / 88 | Пустая выдача, сообщение доставлено |
| 23:16:14 фактически | Nemotron 3 Ultra free | 15,497 | Не получены | HTTP 429, сообщение об ошибке доставлено |

Ниже сохранены ответы каждого запуска, включая ошибки и подавленную отправку. 

## Прогон 1

<details>
<summary>Ответ и запись планировщика</summary>

# Cron Job: paper-digest-check

**Job ID:** 04bbb8d960f3
**Run Time:** 2026-11-17 03:06:52
**Schedule:** 5,10,15 3 * * *

The search results from arXiv over the last 365 days show no papers matching the VKR topic of "web interface adaptation to user behavior and evaluation of effectiveness." The query `web interface adaptation user behavior evaluation` and its variations returned papers on unrelated topics (maritime data fusion, brain-to-text decoding, robotics, video diffusion, etc.). 

The skill's instructions specify: "Если подходящих работ меньше трёх, верни меньше." and "Если записи есть, но ни одна не подходит по смыслу, скажи об этом." None of the 20 retrieved papers from the past year are relevant to adapting web interfaces based on user behavior patterns and evaluating their effectiveness. The closest-adjacent paper is "Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination" (2026-11-13), which deals with web agent hallucinations but not adaptive interface design based on user behavior.

Used query: `web interface adaptation user behavior evaluation` (and variations: `adaptive web user interface behavior personalization`, `interface adaptation user modeling evaluation study`, `human computer interaction adaptive web usability evaluation`, `adaptive interface user study`, `computer human web interaction interface adaptation personalization`, `adaptive "interface" "user" study`). All returned irrelevant results.

[SILENT]

</details>

## Прогон 2

<details>
<summary>Ответ и запись планировщика</summary>

# Cron Job: paper-digest-check

**Job ID:** 04bbb8d960f3
**Run Time:** 2026-11-17 03:11:02
**Schedule:** 5,10,15 3 * * *

На основе скрипта paper-digest запроса `web interface adaptation user behavior` за 365 дней. Выбрал 3 статьи из результатов, соответствующие теме ВКР (методы адаптации веб-интерфейсов под поведение пользователей и оценка эффективности).

**Название статьи**: FETTUCCINE: Fast and efficient brain-to-text decoding on mobile devices  
**Авторы**: Jonathan D. McCart, Pranav I. Deevi, Mehdi Azabou, Nanda H. Krishna, Caleb A. McKinney, Nicholas S. Card, Sergey D. Stavisky, Chethan Pandarinath  
**Дата**: 2026-11-13  
**Ссылка**: https://arxiv.org/abs/2611.18561v1  
**Связь с темой ВКР**: Предлагает end-to-end framework для декодирования neural activity в текст с использованием language models, что relates to adaptive interface behavior under varying user neural states and evaluation of decoding effectiveness.

**Название статьи**: Understanding Contextual Bias in Agricultural CNNs Through Hidden-Neuron Concept Induction  
**Авторы**: Abhilekha Dalal, Avishek Das, Samatha Ereshi Akkamahadevi  
**Дата**: 2026-11-13  
**Ссылка**: https://arxiv.org/abs/2611.18530v1  
**Связь с темой ВКР**: Анализирует, как CNNs эксплуатируют контекстные Bias на изображениях, предлагая метод Concept Induction для выявления интерпретируемых свойств hidden-neuron активаций — метод оценки, применимый к веб-интерфейсам и поведению пользователей.

**Название статьи**: Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination  
**Авторы**: Mohamed Aghzal, Mor Geva, Gregory J. Stein, Ziyu Yao  
**Дата**: 2026-11-13  
**Ссылка**: https://arxiv.org/abs/2611.18514v1  
**Связь с темой ВКР**: Изучает hallucinations LLM-агентов при взаимодействии с веб-страницами, включая оценку эффективности механических методов интерпретируемости — прямая связь с оценкой методов адаптации интерфейсов и поведения пользователей.

Использованный запрос: web interface adaptation user behavior  
Период поиска: 365 дней

[SILENT]

</details>

## Прогон 3

<details>
<summary>Ответ и запись планировщика</summary>

# Cron Job: paper-digest-check

**Job ID:** 04bbb8d960f3
**Run Time:** 2026-11-17 03:17:52
**Schedule:** 5,10,15 3 * * *

I reached the iteration limit and couldn't generate a summary.

</details>

## Прогон 4

<details>
<summary>Ответ и запись планировщика</summary>

# Cron Job: paper-digest-check-v2

**Job ID:** 674886c06e65
**Run Time:** 2026-11-17 11:27:11
**Schedule:** every 5m

Elicitive User Interfaces: Designing How Users Shape Generative Interfaces  
Авторы: Eunhye Kim, Bryan Min, Haijun Xia, Juho Kim  
Дата: 2026-09-20T13:38:37Z  
Ссылка: https://arxiv.org/abs/2609.23642v1  
Связь с темой ВКР: Статья предлагает подход к генерации интерфейсов, адаптирующих техники элицитации под пользователя, задачу и контекст, что напрямую относится к методам адаптации веб-интерфейсов под поведение пользователей.

Human--AI Interactions as First-Class Data: A Formal Interaction Model and Runtime for Explainable AI Collaboration  
Авторы: Michela Taufer, Kin Ng, Ian Lumsden, Aashish Pandey, Rajasi Gore, Angelina Ju, Sukanya Moudgalya, Ewa Deelman, Sai Swaminathan  
Дата: 2026-10-29T13:23:54Z  
Ссылка: https://arxiv.org/abs/2610.40006v1  
Связь с темой ВКР: Работа описывает формальную модель и среду выполнения для захвата взаимодействий пользователя с AI, включая поведенческие метрики, что может служить основой для адаптации веб-интерфейсов.

Say It or Grab It? Conversational Control of UI Adaptations in Mixed Reality  
Авторы: Sina Elahimanesh, Joao Marcelo Evangelista Belo, Isidora Jeknic, Alexander Koller, Anna Maria Feit  
Дата: 2026-10-17T11:30:56Z  
Ссылка: https://arxiv.org/abs/2610.24640v1  
Связь с темой ВКР: Исследуется речевое управление адаптацией интерфейса в смешанной реальности, демонстрируя пользовательский подход к адаптации, применимый к веб-интерфейсам.

Фактический поисковый запрос: cat:cs.HC AND (ti:"web interface" OR ti:"web UI" OR ti:"web user interface" OR ti:"adaptive interface" OR ti:"adaptive UI" OR ti:"adaptive user interface" OR ti:"personalized interface" OR ti:"personalized UI" OR ti:"personalized user interface" OR ti:"user modeling" OR ti:"user behavior" OR ti:"interface adaptation" OR ti:"UI adaptation" OR ti:"layout adaptation" OR ti:"content adaptation" OR ti:"interaction adaptation" OR abs:"web interface" OR abs:"web UI" OR abs:"web user interface" OR abs:"adaptive interface" OR abs:"adaptive UI" OR abs:"adaptive user interface" OR abs:"personalized interface" OR abs:"personalized UI" OR abs:"personalized user interface" OR abs:"user modeling" OR abs:"user behavior" OR abs:"interface adaptation" OR abs:"UI adaptation" OR abs:"layout adaptation" OR abs:"content adaptation" OR abs:"interaction adaptation")  
Период поиска: 365 дней

</details>

## Прогон 5

<details>
<summary>Ответ и запись планировщика</summary>

# Cron Job: paper-digest-check-v2

**Job ID:** 674886c06e65
**Run Time:** 2026-11-17 11:33:06
**Schedule:** every 5m

**From Blind Edits to Verified Repair: Building Trustworthy User-Side LLM Agents for Web Accessibility**  
Авторы: Lily Bundgaard Wanscher, Markus Heidemann Lorensen, Mohammed Ammad Shafiq, Mahyar Tourchi Moghaddam, Mina Alipour  
Дата: 2026-07-26  
Ссылка: https://arxiv.org/abs/2608.24913v1  
Связь с темой ВКР: Работа описывает клиентский агент, адаптирующий веб-страницы через CSS на лету для доступности, с верификацией изменений — прямой пример адаптации веб-интерфейса под потребности пользователя.

**Efficient Personalization of Generative User Interfaces**  
Авторы: Yi-Hao Peng, Jeffrey P. Bigham, Jason Wu  
Дата: 2026-04-10  
Ссылка: https://arxiv.org/abs/2604.09876v2  
Связь с темой ВКР: Исследуется персонализация генерируемых интерфейсов через парные суждения пользователей, с онлайн-оценкой предпочтений — метод адаптации веб-интерфейса под поведение.

**Intelligent Front-End Personalization: AI-Driven UI Adaptation**  
Авторы: Mona Rajhans  
Дата: 2026-02-03  
Ссылка: https://arxiv.org/abs/2602.03154v1  
Связь с темой ВКР: Сравнивает правило-базированную и RL-базированную адаптацию фронтенда в реальном времени, с описанием архитектуры и метрик — полноценный обзор методов адаптации веб-интерфейсов.

---

Поисковый запрос: `cat:cs.HC AND (ti:"adaptive interface" OR ti:"adaptive UI" OR ti:"interface adaptation" OR ti:"UI adaptation" OR ti:"user interface adaptation" OR abs:"adaptive interface" OR abs:"adaptive UI" OR abs:"interface adaptation" OR abs:"UI adaptation" OR abs:"user interface adaptation" OR ti:"adaptive web" OR ti:"web adaptation" OR abs:"adaptive web" OR abs:"web adaptation" OR ti:"personalized interface" OR ti:"personalized UI" OR abs:"personalized interface" OR abs:"personalized UI")`  
Период: 365 дней

</details>

## Прогон 6

<details>
<summary>Ответ и запись планировщика</summary>

# Cron Job: paper-digest-check-v2

**Job ID:** 674886c06e65
**Run Time:** 2026-11-17 11:39:01
**Schedule:** every 5m

[SILENT]

</details>

## Прогон 7

<details>
<summary>Ответ и запись планировщика</summary>

# Cron Job: paper-digest-delivery-check

**Job ID:** 2a5e251a3093
**Run Time:** 2026-11-17 22:40:29
**Schedule:** every 2m

Проверка arXiv: получено 20 записей, отобрано 6

Continuous Behavioral Synthesis for Adaptive Health Dashboards: An LLM-Mediated Architecture Integrating Explicit Preference, Spatial Reorganization, and Attention Allocation Signals
Авторы: Tiziano Santilli, Mina Alipour, Mahyar T. Moghaddam
Дата: 2026-06-25
Ссылка: https://arxiv.org/abs/2606.26937v1
Связь с темой ВКР: Предлагает LLM-архитектуру для непрерывной адаптации веб-дашбордов на основе явных предпочтений, пространственной реорганизации и внимания пользователя.

From Blind Edits to Verified Repair: Building Trustworthy User-Side LLM Agents for Web Accessibility
Авторы: Lily Bundgaard Wanscher, Markus Heidemann Lorensen, Mohammed Ammad Shafiq, Mahyar Tourchi Moghaddam, Mina Alipour
Дата: 2026-07-26
Ссылка: https://arxiv.org/abs/2608.24913v1
Связь с темой ВКР: Описывает пользовательский браузерный агент, адаптирующий веб-страницы через CSS для доступности с верификацией отсутствия регрессий.

Video-Based Detection of squint and cataract for accessibility-aware adaptive web interface rendering
Авторы: Amar Ranjan Dash, Manas Ranjan Patra
Дата: 2026-07-08
Ссылка: https://arxiv.org/abs/2607.07099v1
Связь с темой ВКР: Разрабатывает детекцию нарушений зрения для последующей интеграции с адаптивными веб-интерфейсами под визуальные ограничения пользователя.

The Accessibility Capability Boundary: Operational Limits and Expansion Potential of AI-Generated Browser-Native Accessibility Systems
Авторы: Rizwan Jahangir, Daisuke Ishii
Дата: 2026-05-19
Ссылка: https://arxiv.org/abs/2605.19638v1
Связь с темой ВКР: Формализует границы возможностей AI-систем доступности, генерирующих браузерные адаптации веб-интерфейсов в виде HTML-артефактов.

Comparing LLM-Based Conversational and Graphical Interfaces for Industrial Decision Tasks: An Exploratory Mixed-Methods Study
Авторы: Roberto Figliè, Simone Caputo, Alan Serrano, Tommaso Turchi, Daniele Mazzei
Дата: 2026-05-29
Ссылка: https://arxiv.org/abs/2605.31224v1
Связь с темой ВКР: Сравнивает эффективность конверсационных и графических веб-интерфейсов для задач принятия решений с метриками времени, ошибок и нагрузки.

Blur Effects on User Performance in Target-Pointing Tasks
Авторы: Ryuto Tomihari, Taiki Kinoshita, Yosuke Oba, Shota Yamanaka, Homei Miyashita
Дата: 2026-04-27
Ссылка: https://arxiv.org/abs/2604.24482v1
Связь с темой ВКР: Исследует влияние размытия экрана на производительность указания, предлагая адаптацию веб-интерфейсов под остроту зрения пользователя.

Поисковый запрос: cat:cs.HC AND (ti:"web interface" OR ti:"web page" OR ti:"web UI" OR ti:"user interface" OR abs:"web interface" OR abs:"web page" OR abs:"web UI" OR abs:"user interface") AND (ti:adapt* OR abs:adapt* OR ti:personaliz* OR abs:personaliz* OR ti:"user model" OR abs:"user model" OR ti:"user behavior" OR abs:"user behavior" OR ti:"user modelling" OR abs:"user modelling" OR ti:"user modeling" OR abs:"user modeling")
Период: 365 дней

</details>

## Прогон 8

<details>
<summary>Ответ и запись планировщика</summary>

# Cron Job: paper-digest-validation

**Job ID:** 783145bc8df5
**Run Time:** 2026-11-17 23:10:25
**Mode:** no_agent (script)

---

Проверка arXiv: получено 0, отобрано 0.

За выбранный период подходящих работ в полученной выдаче не найдено.

Запрос: cat:cs.HC AND (ti:"web interface" OR ti:"browser interface" OR abs:"web interface" OR abs:"browser interface") AND (ti:adapt* OR ti:personaliz* OR abs:adapt* OR abs:personaliz*) AND (ti:behavior OR ti:behaviour OR abs:behavior OR abs:behaviour)
Период: 7 суток.

</details>

## Прогон 9

<details>
<summary>Ответ и запись планировщика</summary>

# Cron Job: paper-digest-validation

**Job ID:** 783145bc8df5
**Run Time:** 2026-11-17 23:16:31
**Mode:** no_agent (script)
**Status:** script failed

Script exited with code 1
stdout:
Проверка arXiv: получено 0, отобрано 0.

Проверка не завершена: Ошибка модели на этапе query: HTTP 429: Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day: https://openrouter.ai/settings/credits?utm_source=api&utm_campaign=free_daily_limit
Период: 7 суток.

</details>

## Контрольный запуск

Скрипт запущен командой в Docker. После запуска он сам выполнил поиск и отбор статей. Модель: Nemotron 3 Ultra free; период поиска: 365 суток. Планировщик в этой проверке не использовался.

| Время сценария, с | Входные / выходные токены | Результат |
|---:|---:|---|
| 18,956 | 9 249 / 486 | Из 20 записей выбрана одна; два предложения модели отклонены проверкой |

<details>
<summary>Ответ контрольного запуска</summary>

Проверка arXiv: получено 20, отобрано 1.

Generative UI as an Accessibility Bridge: Lessons from C2C E-Commerce
Авторы: Bektur Ryskeldiev
Дата: 2026-04-28
Ссылка: https://arxiv.org/abs/2604.25455v1
Связь с темой: Генеративный UI создаёт адаптированные интерфейсы в момент использования для преодоления барьеров доступности

Часть предложений модели исключена при проверке данных.

Запрос: cat:cs.HC AND (ti:web OR ti:browser OR abs:web OR abs:browser) AND (ti:"adaptive interface" OR ti:"adaptive UI" OR ti:"personalized interface" OR ti:"personalized UI" OR ti:"user-adaptive" OR ti:"user-adaptive" OR ti:"interface adaptation" OR ti:"UI adaptation" OR abs:"adaptive interface" OR abs:"adaptive UI" OR abs:"personalized interface" OR abs:"personalized UI" OR abs:"user-adaptive" OR abs:"user-adaptive" OR abs:"interface adaptation" OR abs:"UI adaptation" OR ti:"user behavior" OR ti:"user modelling" OR ti:"user modeling" OR abs:"user behavior" OR abs:"user modelling" OR abs:"user modeling" OR ti:"rule-based" OR ti:"machine learning" OR ti:"reinforcement learning" OR abs:"rule-based" OR abs:"machine learning" OR abs:"reinforcement learning")
Период: 365 суток.

</details>


## Проверка расписания 18 ноября

Три запуска задания `paper-digest-final-check` (`2f483d8aaaf3`) выполнены планировщиком на VPS в 03:05, 03:15 и 03:25 МСК. Модель — Nemotron 3 Ultra free; период поиска — семь суток. Время выполнения и токены взяты из записей сценария, приведённых в таблице P2.

### Ночной запуск 1

<details>
<summary>Ответ планировщика</summary>

# Cron Job: paper-digest-final-check

**Job ID:** 2f483d8aaaf3
**Run Time:** 2026-11-18 03:05:29
**Mode:** no_agent (script)

---

Проверка arXiv: получено 0, отобрано 0.

За выбранный период подходящих работ в полученной выдаче не найдено.

Запрос: cat:cs.HC AND (ti:web OR ti:browser OR abs:web OR abs:browser) AND (ti:"adaptive interface" OR ti:"adaptive ui" OR ti:"user interface adaptation" OR ti:"interface personalization" OR ti:"ui personalization" OR ti:"adaptive web" OR abs:"adaptive interface" OR abs:"adaptive ui" OR abs:"user interface adaptation" OR abs:"interface personalization" OR abs:"ui personalization" OR abs:"adaptive web" OR ti:"rule-based adaptation" OR ti:"machine learning adaptation" OR abs:"rule-based adaptation" OR abs:"machine learning adaptation" OR ti:"hybrid adaptation" OR abs:"hybrid adaptation")
Период: 7 суток.

</details>

### Ночной запуск 2

<details>
<summary>Ответ планировщика</summary>

# Cron Job: paper-digest-final-check

**Job ID:** 2f483d8aaaf3
**Run Time:** 2026-11-18 03:15:26
**Mode:** no_agent (script)

---

Проверка arXiv: получено 1, отобрано 0.

За выбранный период подходящих работ в полученной выдаче не найдено.

Запрос: cat:cs.HC AND (ti:"web interface" OR ti:"browser interface" OR abs:"web interface" OR abs:"browser interface" OR abs:"web-based interface") AND (ti:adapt* OR ti:personaliz* OR abs:adapt* OR abs:personaliz* OR ti:"user modeling" OR abs:"user modeling" OR ti:"behavior-based" OR abs:"behavior-based" OR ti:"behaviour-based" OR abs:"behaviour-based")
Период: 7 суток.

</details>

### Ночной запуск 3

<details>
<summary>Ответ планировщика</summary>

# Cron Job: paper-digest-final-check

**Job ID:** 2f483d8aaaf3
**Run Time:** 2026-11-18 03:25:26
**Mode:** no_agent (script)

---

Проверка arXiv: получено 0, отобрано 0.

За выбранный период подходящих работ в полученной выдаче не найдено.

Запрос: cat:cs.HC AND (abs:"web interface" OR abs:"browser interface" OR abs:"web UI" OR abs:"browser-based") AND (abs:"adaptive interface" OR abs:"adaptive UI" OR abs:"interface adaptation" OR abs:"UI adaptation" OR abs:"personalization" OR abs:"personalised interface" OR abs:"personalized interface" OR abs:"user-adaptive" OR abs:"behavior-based adaptation" OR abs:"behaviour-based adaptation" OR abs:"user behavior adaptation" OR abs:"user behaviour adaptation") AND (abs:"rule-based" OR abs:"machine learning" OR abs:"ML-based" OR abs:"reinforcement learning" OR abs:"supervised learning" OR abs:"hybrid" OR abs:"combined approach")
Период: 7 суток.

</details>
