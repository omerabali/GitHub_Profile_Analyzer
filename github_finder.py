from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>GitHub Profil Analiz Aracı</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body { background: #0d1117; color: #f0f0f0; font-family: Arial; }
        .card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; }
        .btn-custom { background: #238636; color: white; }
        .btn-custom:hover { background: #2ea043; }
        .profile-img { width: 150px; height: 150px; border-radius: 50%; border: 3px solid #30363d; }
        .section-title { font-size: 22px; margin-top: 40px; margin-bottom: 20px; color: #c9d1d9; }
        .search-card:hover { background: #1c2128; transition: .2s; }
        .profile-info p { color: #e3e6e8; font-size: 16px; }
        .profile-info strong { color: #ffffff; }

        /* Stat Kartları */
        .stat-card {
            background: #21262d;
            border-radius: 10px;
            flex: 1;
            margin: 0 5px;
            color: #f5f5f5;
            transition: 0.2s;
            cursor: default;
            padding: 10px 0;
        }
        .stat-card:hover {
            background: #2d333b;
            transform: translateY(-3px);
        }
    </style>
</head>
<body>

<div class="container mt-4">

    <h2 class="text-center mb-4">🔍 GitHub Profil Analiz Aracı</h2>

    <!-- ARAMA MOTORU -->
    <div class="card p-3 mb-4">
        <form method="POST">
            <label><strong>GitHub Kullanıcı Adı:</strong></label>
            <input type="text" name="username" class="form-control mb-3" placeholder="username veya kelime..." required>

            <div class="d-flex gap-2">
                <button class="btn btn-custom w-50" name="mode" value="profile">Profil Ara</button>
                <button class="btn btn-primary w-50" name="mode" value="search">Kullanıcıları Ara</button>
            </div>
        </form>
    </div>

    {% if search_results %}
        <h3 class="section-title">🔎 Arama Sonuçları</h3>
        <div class="row">
        {% for item in search_results %}
            <div class="col-md-4">
                <a href="/?user={{ item.login }}" style="text-decoration:none;">
                    <div class="card p-3 mb-3 search-card">
                        <img src="{{ item.avatar_url }}" class="profile-img mx-auto d-block" style="width:110px;height:110px;">
                        <h4 class="text-center mt-2">{{ item.login }}</h4>
                    </div>
                </a>
            </div>
        {% endfor %}
        </div>
    {% endif %}

    {% if profile %}
    <!-- PROFIL KARTI -->
    <div class="card p-4 mx-auto profile-info" style="max-width: 700px;">
        <div class="text-center">
            <img src="{{ profile.avatar_url }}" class="profile-img">
            <h3 class="mt-3">{{ profile.name }}</h3>
            <p class="text-secondary">{{ profile.login }}</p>
        </div>

        <p><strong>Bio:</strong> {{ profile.bio }}</p>
        <p><strong>Konum:</strong> {{ profile.location }}</p>
        <p><strong>Şirket:</strong> {{ profile.company }}</p>

        <!-- REPO / TAKİPÇİ / TAKİP EDİLEN Kartları -->
        <div class="d-flex justify-content-between mt-4">
            <div class="stat-card text-center">
                <div style="font-size:24px;">📁</div>
                <div><strong>{{ profile.public_repos }}</strong></div>
                <div>Repolar</div>
            </div>
            <div class="stat-card text-center">
                <div style="font-size:24px;">⭐</div>
                <div><strong>{{ profile.followers }}</strong></div>
                <div>Takipçi</div>
            </div>
            <div class="stat-card text-center">
                <div style="font-size:24px;">➡</div>
                <div><strong>{{ profile.following }}</strong></div>
                <div>Takip Edilen</div>
            </div>
        </div>

        <a href="{{ profile.html_url }}" class="btn btn-custom w-100 mt-3" target="_blank">GitHub Profiline Git</a>
    </div>
    {% endif %}

</div>

</body>
</html>
"""

#### API FUNCTIONS ####

def get_profile(username):
    r = requests.get(f"https://api.github.com/users/{username}")
    return None if r.status_code != 200 else r.json()

def search_users(q):
    r = requests.get(f"https://api.github.com/search/users?q={q}")
    return [] if r.status_code != 200 else r.json().get("items", [])


@app.route("/", methods=["GET", "POST"])
def home():
    profile = None
    search_results = None

    # URL üzerinden kullanıcı açma ör: /?user=torvalds
    username_url = request.args.get("user")
    if username_url:
        profile = get_profile(username_url)

    # POST arama işlemleri
    if request.method == "POST":
        username = request.form.get("username")
        mode = request.form.get("mode")

        # Kullanıcı Profil Arama
        if mode == "profile":
            profile = get_profile(username)

        # Kullanıcı Arama Motoru
        elif mode == "search":
            search_results = search_users(username)

    return render_template_string(TEMPLATE,
                                  profile=profile,
                                  search_results=search_results)


if __name__ == "__main__":
    app.run(debug=True)










#http://127.0.0.1:5000 çalıştırma adresi bu