# 🎵 Music Genre Tagging: Accuracy You Can Trust Across Every Genre

> 🚧 **Work in progress.** Part 1 (data exploration) is complete. Modelling, the client report and the Power BI dashboard are coming next.

**Client question:** A music streaming service wants to automatically tag the genre of new songs. *How accurate would it be, and is it reliable for every genre, not just the common ones?*

**Data:** 8,111 songs from the Free Music Archive across 5 genres (Rock, Electronic, Hip-Hop, Folk, Classical), each with 237 numeric audio and popularity features.

---

## 📌 Findings so far

**1. The genres are heavily imbalanced, so plain accuracy would mislead.**
Rock makes up 48% of songs and Classical only 3%. A model that always guesses "Rock" would score 48% accuracy while failing every other genre. Models in this project are therefore judged on **macro-F1** and **per-genre recall**.

![Genre balance](images/genre_balance.png)

**2. Each genre has a distinct sound profile.**
Classical is almost purely acoustic with very low energy. Hip-Hop has more than double the speechiness of any other genre. Electronic is the most instrumental and least acoustic. Rock sits in the middle on most features, which is where confusion between genres is most likely.

![Genre sound profiles](images/genre_sound_profiles.png)

---

## 🗺️ Project plan

- [x] **Part 1 – Data exploration:** load and name the columns, quality checks, genre balance, sound profiles
- [ ] **Part 2 – Modelling:** baselines, imbalance handling, tuned gradient boosting, every experiment reproducible
- [ ] **Part 3 – Client report:** per-genre reliability and recommendations for using the model in production
- [ ] **Part 4 – Power BI dashboard:** genre profiles and model performance

## 🗂️ Structure

```
music-genre-analysis/
├── data/raw/music.csv                     # original data (no header row)
├── notebooks/01_data_exploration.ipynb    # Part 1
├── images/                                # charts used in this README
└── requirements.txt
```

## ▶️ How to run

```bash
git clone https://github.com/abir110/music-genre-analysis.git
cd music-genre-analysis
pip install -r requirements.txt
jupyter lab notebooks/01_data_exploration.ipynb
```

## 📚 About the data

Extract from the Free Music Archive (Defferrard et al., 2017, *FMA: A Dataset for Music Analysis*), provided for the classification coursework in my MSc Data Science *Machine Learning* module at Aston University. The file has no column names. I mapped them to the FMA Echonest feature set (8 audio descriptors, 5 popularity scores and 224 temporal features) and confirmed the mapping from the value ranges.

---

**Author:** Abir Alam Srabon · [LinkedIn](https://www.linkedin.com/in/abir-alam-srabon) · [Portfolio](https://abir110.github.io)
