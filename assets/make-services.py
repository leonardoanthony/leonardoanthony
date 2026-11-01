"""Faixa de serviços: ícones acendendo em sequência e o nome do serviço sendo
digitado embaixo, sincronizado. Ícones = src/components/icons/service-icons.tsx
do leonardoanthony.dev. Rodar: python3 -I make-services.py (gera services.svg)."""
from pathlib import Path

ICONS = {
    "site": '<rect x="3" y="4" width="18" height="13" rx="1.5"/><path d="M8 21h8M12 17v4M3 8h18"/>',
    "sistema": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    "automacao": '<circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="18" r="2"/><path d="M7 6h10M6 8l5 8M18 8l-5 8"/>',
    "integracao": '<path d="M9 3v4M15 3v4M7 7h10v4a5 5 0 0 1-10 0zM12 16v5"/>',
    "dashboard": '<path d="M3 21h18M6 17v-5M11 17V6M16 17v-3M21 17V9"/>',
    "crm": '<rect x="3" y="4" width="5" height="16" rx="1"/><rect x="10" y="4" width="5" height="11" rx="1"/><rect x="17" y="4" width="4" height="7" rx="1"/>',
    "ecommerce": '<path d="M3 4h2.2l2.1 10.1a1.6 1.6 0 0 0 1.6 1.3h8.3a1.6 1.6 0 0 0 1.6-1.2L21 8H6.1"/><circle cx="9.5" cy="19.5" r="1.3"/><circle cx="17" cy="19.5" r="1.3"/>',
}
SERVICES = [
    ("site", "Site ou landing page"),
    ("sistema", "Sistema ou produto web"),
    ("automacao", "Automação e martech"),
    ("integracao", "Integração e tracking"),
    ("dashboard", "Dashboard de dados"),
    ("crm", "CRM e funil de vendas"),
    ("ecommerce", "Loja virtual"),
]

W, H = 1200, 186
STEP = 2.6                     # segundos por serviço
N = len(SERVICES); CYCLE = STEP * N
TW, TH, GAP, TY = 80, 72, 20, 12
X0 = (W - (N * TW + (N - 1) * GAP)) / 2
FS = 28; CW = FS * 0.6         # largura de caractere monoespaçado
TEXT_Y = 156
T_CHAR, T_ERASE_CHAR = 0.055, 0.02
ON_PCT = 100 / N; OFF_PCT = ON_PCT + 3


def f(x):
    return f"{x:.4f}".rstrip("0").rstrip(".")


tiles, typed = [], []
for i, (sid, name) in enumerate(SERVICES):
    x = X0 + i * (TW + GAP); d = i * STEP
    tiles.append(
        f'<g transform="translate({f(x)} {TY})">'
        f'<rect class="t" style="animation-delay:{f(d)}s" width="{TW}" height="{TH}" rx="14"/>'
        f'<g class="ic" style="animation-delay:{f(d)}s" transform="translate(25 21) scale(1.25)" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[sid]}</g></g>'
    )
    # tempos dentro do ciclo: digita, segura, apaga
    n = len(name); full = n * CW
    start_x = W / 2 - (full + 2 + CW) / 2   # centraliza texto + cursor
    times, widths = [0.0], [0.0]
    for k in range(1, n + 1):
        times.append(k * T_CHAR); widths.append(k * CW)
    hold_end = STEP - 0.25 - n * T_ERASE_CHAR
    for k in range(n - 1, -1, -1):
        times.append(hold_end + (n - k) * T_ERASE_CHAR); widths.append(k * CW)
    times.append(CYCLE); widths.append(0.0)
    kt = ";".join(f(t / CYCLE) for t in times)
    wv = ";".join(f(w) for w in widths)
    cx = ";".join(f(start_x + w + 2) for w in widths)
    typed.append(f'''
    <clipPath id="c{i}"><rect x="{f(start_x)}" y="{TEXT_Y - FS}" width="0" height="{FS + 8}">
      <animate attributeName="width" values="{wv}" keyTimes="{kt}" calcMode="discrete" dur="{f(CYCLE)}s" begin="{f(d)}s" repeatCount="indefinite"/></rect></clipPath>
    <text x="{f(start_x)}" y="{TEXT_Y}" class="mono" font-size="{FS}" font-weight="500" fill="#f2774a" clip-path="url(#c{i})" textLength="{f(full)}" lengthAdjust="spacingAndGlyphs">{name}</text>
    <rect class="cur" y="{TEXT_Y - FS + 3}" width="11" height="{FS + 2}" fill="#ea5c2d" opacity="0" x="{f(start_x + 2)}">
      <animate attributeName="x" values="{cx}" keyTimes="{kt}" calcMode="discrete" dur="{f(CYCLE)}s" begin="{f(d)}s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0;0" keyTimes="0;{f(STEP / CYCLE)};1" calcMode="discrete" dur="{f(CYCLE)}s" begin="{f(d)}s" repeatCount="indefinite"/>
    </rect>''')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Serviços: {", ".join(n for _, n in SERVICES)}">
  <style>
    .mono{{font-family:"JetBrains Mono",SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace}}
    .t{{fill:#fff;fill-opacity:.04;stroke:#fff;stroke-opacity:.1;animation:t {f(CYCLE)}s infinite}}
    @keyframes t{{0%,{f(ON_PCT)}%{{fill:#ea5c2d;fill-opacity:.18;stroke:#ea5c2d;stroke-opacity:.6}}{f(OFF_PCT)}%,100%{{fill:#fff;fill-opacity:.04;stroke:#fff;stroke-opacity:.1}}}}
    .ic{{stroke:#8a8a96;animation:ic {f(CYCLE)}s infinite}}
    @keyframes ic{{0%,{f(ON_PCT)}%{{stroke:#f2774a}}{f(OFF_PCT)}%,100%{{stroke:#8a8a96}}}}
  </style>
  {"".join(tiles)}{"".join(typed)}
</svg>
'''
Path(__file__).with_name("services.svg").write_text(svg)
print(f"services ok (ciclo {f(CYCLE)}s)")
