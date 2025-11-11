# Farmeasy

**AI software for Farmer Query Support and Advisory System**

---

##  Overview

Farmeasy is a lightweight, farmer-focused AI assistant designed to help smallholder and commercial farmers make better decisions quickly and confidently. Beyond the code, Farmeasy is built to close the information gap between modern agricultural knowledge and the farmer in the field — providing clear, localized, and practical advice about crop care, pest management, fertilization, post-harvest handling, and weather-aware planning.

This repository contains the ingestion, preprocessing, vector store, and API/CLI glue-code to prototype a farmer-support assistant.

---

## Impact on farmers' lives 

Farmeasy is more than software — it's a practical helper for everyday farming problems. Here’s how it can improve lives:

* **Faster, more confident decisions:** Instead of waiting for an extension worker or searching multiple sources, farmers can get immediate, easy-to-understand answers—e.g., how to treat a crop disease today or whether to delay irrigation because of expected rain.
* **Reduced crop losses:** By giving timely pest and disease management steps (symptoms to look for, low-cost remedies, and safety instructions), Farmeasy helps prevent small problems from becoming yield-destroying issues.
* **Cost savings:** The assistant recommends solutions with cost and availability in mind (e.g., locally available inputs or low-cost organic alternatives), helping farmers avoid unnecessary or expensive treatments.
* **Improved yields and income:** Better management leads to healthier crops and higher quality produce, which translates to better market prices and more stable income.
* **Increased knowledge & independence:** Farmers learn practical techniques through simple explanations and step-by-step guidance — building long-term self-reliance rather than one-off help.
* **Accessibility:** Farmeasy can be adapted to different languages and literacy levels (short, plain-language answers, and potentially voice interfaces) so more farmers can use it.

These benefits particularly help smallholder farmers who often lack fast access to current agronomic advice.

---

##  What makes Farmeasy better than a generic AI chatbot

Generic chatbots are powerful but often miss critical requirements for real-world farming support. Farmeasy is purpose-built — here’s how it stands out:

1. **Domain-focused knowledge:** Farmeasy is tuned to agricultural documents (extension guides, research notes, product labels, local advisories), so its responses are grounded in farming best practices rather than general internet text.
2. **Retrieval-augmented answers:** Instead of hallucinating, Farmeasy looks up the most relevant local documents and returns answers supported by real sources. That means higher factual accuracy and traceability.
3. **Actionable, safety-first guidance:** Farmeasy prioritizes practical steps and safety (for chemical use, handling PPE, or safe disposal) rather than vague or purely theoretical advice.
4. **Localizability:** The system is designed to accept local manuals and advisories. That enables region-specific advice — for example, pest names and recommended sprays differ by region and season, and Farmeasy can reflect that.
5. **Lightweight & offline-friendly options:** The architecture supports local vector stores and can be adapted to low-bandwidth deployments (e.g., a nearby edge server, on-device embeddings), making the tool usable where internet access is limited.
6. **Tested, explainable responses:** With a vector store and citation-like retrieval, Farmeasy can point to the documents (or document snippets) that informed its answer. This transparency builds trust with users.

---

## ✨ Uniqueness & Advantages (what sets Farmeasy apart)

* **Farmer-centered UX & outputs:** Answers are written to be concise, concrete, and action-oriented ("What to do now", "Materials needed", "When to call an expert"), not academic.
* **Source-backed recommendations:** Because the assistant retrieves and cites local documents, extension officers and NGOs can audit and verify recommendations easily.
* **Flexible deployment:** Use it as a command-line tool for quick experiments, a lightweight API for integration into mobile apps, or as the backend for a voice agent in low-literacy communities.
* **Cost-aware suggestions:** The system can be configured to prioritize low-cost, widely available solutions — important for resource-constrained farmers.
* **Privacy-first by design:** Sensitive farm data need not leave a local installation; you can run the vector store locally or on a private server to preserve farmer privacy.
* **Modular & extensible:** Swap embedding models, add new agricultural datasets, or plug in external services (weather, market prices) with minimal changes.

---

## 🛠️ How Farmeasy actually helps — a short, non-technical walkthrough

1. **You give the system your documents:** local extension guides, leaflets, regional advisories, or PDF manuals.
2. **Farmeasy turns those into searchable knowledge:** it cleans the text, splits it into small pieces (chunks), and builds a searchable index.
3. **A farmer asks a question:** for example, "My tomato leaves have dark spots and the lower leaves are yellowing — what should I do?"
4. **Farmeasy searches its index:** it finds the best-matching document excerpts about similar symptoms and treatments.
5. **It replies with a practical plan:** e.g., identify likely disease, list steps to confirm diagnosis, low-cost treatment options, safety notes, and when to seek help — plus the document snippets it used.

This makes answers fast, actionable, and traceable.

---

## 📈 Example real-world impact scenarios

* **Smallholder farmer in a rain-fed region:** Receives a notification to delay irrigation because of an incoming weather advisory and saves labor and water.
* **Cooperative extension officer:** Uses Farmeasy to prepare a short, accurate advisory sheet for members before a festival season when certain pests spike.
* **Market-oriented grower:** Follows post-harvest handling steps suggested by Farmeasy to reduce spoilage and improve market grade — boosting income.

---

## ⚡ Getting Started (Local)

> These commands assume you have Python 3.8+ and `git` installed.

1. Clone the repository

```bash
git clone https://github.com/PranoyRoy2004/Farmeasy.git
cd Farmeasy
```

2. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv/Scripts/Activate.ps1  # Windows (PowerShell) - use forward slashes in the README for portability
```

3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Add agricultural documents to ./data and run ingestion

```bash
python ingestion.py --data-dir ./data
python vectorstore.py --build
python main.py
```

---

## 🧪 Tests

Run tests with `pytest`:

```bash
pytest -q
```

---

## 📜 Ethics & Safety

* **Avoiding unsafe medical/agricultural advice:** The system focuses on agronomy and practical farm management. For severe plant disease or human/animal health issues, Farmeasy recommends contacting certified extension agents or veterinarians.
* **Privacy:** Deployments can keep data local. The default code does not send farmer data to third parties unless configured to do so.
* **Bias & source quality:** Farmeasy’s answers are only as good as the data fed into it. Use trusted extension publications and validated manuals to reduce risk of poor recommendations.

---

## ✅ Contributing

Contributions are welcome! Please open an issue or a pull request with a clear description of the change. Suggested workflow:

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Make changes and add tests
4. Run tests locally
5. Open a pull request with a description of what you changed and why

---

## 📬 Contact

Maintainer: **Pranoy Roy**

If you'd like help extending this project — adding a mobile UI, deploying to low-bandwidth environments, or integrating weather and market data — open an issue or message me on GitHub.

---

*Updated README with plain-language impact, uniqueness, and advantages. Ask me to localize the language for a particular region or to add sample dialog examples for farmer interactions.*

