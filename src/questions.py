import random

# List pertanyaan untuk simulasi load test
QUESTIONS = [
    "Apa itu AI?",
    "Jelaskan machine learning dalam 1 paragraf.",
    "Apa perbedaan supervised dan unsupervised learning?",
    "Bagaimana cara kerja neural network?",
    "Apa itu LLM?",
    "Sebutkan aplikasi AI di kehidupan sehari-hari.",
    "Bagaimana AI bisa membantu bisnis retail?",
    "Apa tantangan utama dalam pengembangan AI?",
    "Jelaskan konsep reinforcement learning.",
    "Apa itu overfitting dan bagaimana mengatasinya?",
    "Bagaimana AI digunakan dalam bidang kesehatan?",
    "Apa itu NLP?",
    "Jelaskan proses training model AI.",
    "Apa itu data labeling?",
    "Bagaimana cara memilih model AI yang tepat?",
    "Apa itu transfer learning?",
    "Jelaskan peran data dalam AI.",
    "Apa itu deep learning?",
    "Bagaimana AI bisa digunakan untuk prediksi cuaca?",
    "Apa itu chatbot?",
    "Jelaskan perbedaan AI dan automation.",
    "Bagaimana AI mempengaruhi industri manufaktur?",
    "Apa itu computer vision?",
    "Bagaimana AI digunakan dalam e-commerce?",
    "Apa itu model generatif?",
    "Jelaskan ethical AI.",
    "Bagaimana AI bisa membantu pendidikan?",
    "Apa itu supervised learning?",
    "Bagaimana cara kerja recommendation system?",
    "Apa itu data mining?",
    "Jelaskan AI dalam bidang transportasi.",
    "Apa itu model prediktif?",
    "Bagaimana AI digunakan dalam keamanan siber?",
    "Apa itu explainable AI?",
    "Bagaimana AI bisa membantu pertanian?",
    "Apa itu anomaly detection?",
    "Jelaskan AI dalam bidang keuangan.",
    "Bagaimana AI digunakan dalam game?",
    "Apa itu unsupervised learning?",
    "Bagaimana AI bisa membantu pengambilan keputusan?",
    "Apa itu model regresi?",
    "Jelaskan AI dalam bidang energi.",
    "Bagaimana AI digunakan dalam analisis sentimen?",
    "Apa itu model klasifikasi?",
    "Bagaimana AI bisa membantu pemerintah?",
    "Apa itu data preprocessing?",
    "Jelaskan AI dalam bidang logistik.",
    "Bagaimana AI digunakan dalam deteksi penipuan?",
    "Apa itu model clustering?",
    "Bagaimana AI bisa membantu lingkungan?"
    ,"Apa peran AI dalam pengembangan smart city?"
    ,"Bagaimana AI digunakan untuk deteksi penyakit dini?"
    ,"Apa tantangan data privacy dalam AI?"
    ,"Bagaimana AI membantu dalam pengolahan citra medis?"
    ,"Apa itu federated learning?"
    ,"Bagaimana AI digunakan dalam prediksi harga saham?"
    ,"Apa itu model sequence-to-sequence?"
    ,"Bagaimana AI membantu dalam pengenalan suara?"
    ,"Apa itu GAN (Generative Adversarial Network)?"
    ,"Bagaimana AI digunakan dalam sistem rekomendasi musik?"
    ,"Apa itu edge AI?"
    ,"Bagaimana AI membantu dalam pengelolaan supply chain?"
    ,"Apa itu data augmentation?"
    ,"Bagaimana AI digunakan dalam analisis video?"
    ,"Apa itu one-shot learning?"
    ,"Bagaimana AI membantu dalam mitigasi bencana?"
    ,"Apa itu reinforcement learning dalam robotika?"
    ,"Bagaimana AI digunakan dalam analisis sentimen media sosial?"
    ,"Apa itu transfer learning dan contohnya?"
    ,"Bagaimana AI membantu dalam deteksi spam email?"
    ,"Apa itu model transformer?"
    ,"Bagaimana AI digunakan dalam autonomous vehicle?"
    ,"Apa itu zero-shot learning?"
    ,"Bagaimana AI membantu dalam pengelolaan energi terbarukan?"
    ,"Apa itu self-supervised learning?"
    ,"Bagaimana AI digunakan dalam analisis perilaku konsumen?"
    ,"Apa itu model attention?"
    ,"Bagaimana AI membantu dalam pengembangan chatbot multibahasa?"
    ,"Apa itu continual learning?"
    ,"Bagaimana AI digunakan dalam prediksi permintaan pasar?"
    ,"Apa itu explainability dalam AI dan mengapa penting?"
    ,"Bagaimana AI membantu dalam pengembangan aplikasi mobile?"
    ,"Apa itu model ensemble dalam machine learning?"
    ,"Bagaimana AI digunakan dalam pengenalan wajah?"
    ,"Apa itu data imbalance dan bagaimana mengatasinya?"
    ,"Bagaimana AI membantu dalam pengembangan game edukasi?"
    ,"Apa itu model probabilistik dalam AI?"
    ,"Bagaimana AI digunakan dalam optimasi logistik?"
    ,"Apa itu adversarial example dalam AI?"
    ,"Bagaimana AI membantu dalam pengembangan sistem keamanan?"
    ,"Apa itu model bayesian?"
    ,"Bagaimana AI digunakan dalam pengolahan bahasa alami (NLP)?"
    ,"Apa itu active learning?"
    ,"Bagaimana AI membantu dalam pengembangan sistem rekomendasi film?"
    ,"Apa itu semi-supervised learning?"
    ,"Bagaimana AI digunakan dalam prediksi cuaca ekstrem?"
    ,"Apa itu model decision tree?"
    ,"Bagaimana AI membantu dalam pengembangan teknologi wearable?"
    ,"Apa itu hyperparameter tuning dalam AI?"
    ,"Bagaimana AI digunakan dalam pengembangan sistem deteksi intrusi?"
    ,"Apa itu model random forest?"
    ,"Bagaimana AI membantu dalam pengembangan sistem monitoring kesehatan?"
    ,"Apa itu feature engineering dalam machine learning?"
    ,"Bagaimana AI digunakan dalam pengembangan sistem rekomendasi buku?"
]

# Fungsi untuk mengambil pertanyaan random
def get_random_question():
    return random.choice(QUESTIONS)
