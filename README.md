# Přehled změn

### Globální změny (opakují se ve všech adresářích)

**Dockerfiles — base image** Všechny Dockerfiles z `debian:latest` na `debian:11-slim`

**Dockerfiles — čistění apt cache** `apt purge -y --auto-remove` nahrazeno `apt-get clean && rm -rf /var/lib/apt/lists/*`

**Dockerfiles — uživatel asterisk** `--home /home/asterisk` - přidán správný domovský adresář

**Dockerfiles — CMD** Úprava shell formátu `CMD asterisk -f` na `CMD ["asterisk", "-f"]`

**postgres/Dockerfile** Inicializační SQL ze složky `init/` (`COPY init/*.sql` a `COPY init/*.sh`) - Pro automatickou inicializaci skriptů z této složky

**compose.yaml — Kontrola databáze** `depends_on: database: condition: service_healthy`. Healthcheck pro PostgreSQL kontejner (`pg_isready`), takže Asterisk čeká na připravenou databázi, ne jen spuštěný kontejner

**compose.yaml — volumes** Absolutní bind mount `/database:/var/lib/postgresql/data` byl nahrazen pojmenovaným volume `postgres_data:`, ten je v sekci `volumes:`. Data díky tomu přežijí `docker compose down` bez nutnosti spravovat absolutní cestu na hostu

**compose.yaml — oprávnění** Bind mounty mají přidán `:z` suffix pro správné SELinux labeling

**compose.yaml — odstraněno `version:`** Docker Compose ho ignoruje nově

---
### Adresář `01-initial_setup`

**Dockerfile** navíc:

- Verze Asterisk změněna z `20.5.2` na `20.6.0`.
- Přidán blok `COPY asterisk/ /etc/asterisk/` — konfigurace se nyní kopíruje přímo do image místo generování `make samples`
- Oprávnění nastavena na `/var/lib/asterisk`, `/var/log/asterisk`, `/var/run/asterisk` (přidány chybějící adresáře)
- Odstraněno zbytečné nastavení `chown` přes wildcard `/var/*/asterisk`
- Odstraněny zakomentované řádky (`# COPY get_sounds.sh`, `# make samples`, atd.)

---

### Adresář `02-two_stage`

**Dockerfile** navíc:

- Builder stage doplněna o nové build závislosti: `libopus-dev`, `libjansson-dev`, `libncurses5-dev`, `libtinfo-dev`, `libunwind-dev`, `cmake`, `pkg-config`
- Opravena chybná závislost `libxslt1-dev` → `libxslt-dev`, `uuid` + `uuid-dev` → `uuid-runtime`.
- Final stage nyní kopíruje konfiguraci z builder stage: `COPY --from=builder --chown=asterisk:asterisk /etc/asterisk/ /etc/asterisk/`

---

### Adresář `03-compose`

**Nový soubor `.env`** — Původně byl až v branchi 04

---

### Adresář `04-ami`

**asterisk/etc/asterisk/manager.conf** Zakomentovaný řádek `;permit=209.16.236.73/255.255.255.0` byl nahrazen aktivním `permit=0.0.0.0/0.0.0.0` — AMI nyní povoluje připojení ze všech adres (vhodné pro Docker síť)

**asterisk/etc/asterisk/modules.conf** Přidáno explicitní načtení `load = res_manager.so` — zajistí, že AMI modul je vždy načten

**scripts/originate.py** — největší změna v tomto adresáři:

- Přidán `import sys`
- Odstraněna třída `AmiContextManager` (context manager vzor) — nahrazena přímou správou připojení s explicitní kontrolou chyb
- Přidány nové CLI parametry `--host`, `--port`, `--timeout` — skript je nyní flexibilnější
- Přidán `show_default=True` u existujících parametrů
- Opravena chyba: `Channel` byl `Local/{from_ext}@from-ami` (volající), nyní správně `Local/{to_ext}@from-ami` (volaný). Zároveň opraveno `CallerID` — nyní zobrazuje `from_ext`
- Přidána kontrola návratových hodnot AMI (`response.status == "Error"`)
- Přidáno ošetření výjimek (`ConnectionRefusedError`) s informativními chybovými výstupem

---

### Adresář `05-all-elements`

**compose.yaml**

- Odstraněno `expose: - 5038` (AMI port)
- Služba `fastapi` nyní má explicitní spuštění `uvicorn voip2_backend.main:app --host 0.0.0.0 --port 8080`

**fastapi/Dockerfile** 

- Single-stage build oproti buildu+production
- Odstraněna správa virtualenv (`$VENV_PATH`) — závislosti se instalují globálně (`poetry config virtualenvs.create false`)
- Poetry instaluje závislosti bez root balíčku (`--no-root`)
- Přidána explicitní instalace `uvicorn`
- Aplikační kód se kopíruje přímo (`COPY voip2_backend voip2_backend`)
- Opraven port z `80` na `8080`
- Odstraněny build argumenty (`ARG db_url` a `ENV DATABASE_URL`)

**fastapi/voip2_backend/lib/** — nová složka s moduly `ami.py` a `schemas.py`.

**nginx/Dockerfile** Přidán řádek `COPY ./etc/click2dial.html /usr/share/nginx/html` — do image se nyní kopíruje html web

**nginx/etc/nginx/nginx.conf**

- Přidán `location /` blok, který nastaví nový `click2dial.html` jako hlavní stránku (přes `try_files`)

**nginx/etc/click2dial.html** — Click2Dial webová aplikace viz obrázek

**scripts/originate.py** — Původně chyběl

---

![Click2Dial](https://github.com/Krupis294/voip2/blob/main/fig/Click2Dial.png)
