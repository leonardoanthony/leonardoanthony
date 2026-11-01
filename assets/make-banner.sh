#!/bin/bash
# Banner centralizado: nome, título e números do portfolio.
cd "$(dirname "$0")"
W=1200; H=310
cat > banner.svg <<EOF
<svg xmlns="http://www.w3.org/2000/svg" width="$W" height="$H" viewBox="0 0 $W $H" role="img" aria-label="Leonardo Anthony — Dev full-stack e Martech Engineer">
  <defs>
    <radialGradient id="glow" cx="50%" cy="70%" r="55%">
      <stop offset="0" stop-color="#ea5c2d" stop-opacity=".24"/>
      <stop offset=".55" stop-color="#ea5c2d" stop-opacity=".05"/>
      <stop offset="1" stop-color="#ea5c2d" stop-opacity="0"/>
    </radialGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#fff" fill-opacity=".06"/></pattern>
    <clipPath id="r"><rect width="$W" height="$H" rx="18"/></clipPath>
  </defs>
  <style>
    .sans{font-family:Inter,"Segoe UI",-apple-system,Helvetica,Arial,sans-serif}
    .mono{font-family:"JetBrains Mono",SFMono-Regular,Menlo,Consolas,monospace}
    .in{opacity:0;animation:in .8s ease-out forwards}
    .d1{animation-delay:.1s}.d2{animation-delay:.35s}.d3{animation-delay:.6s}
    @keyframes in{from{opacity:0}to{opacity:1}}
  </style>
  <g clip-path="url(#r)">
    <rect width="$W" height="$H" fill="#0e0e11"/>
    <rect width="$W" height="$H" fill="url(#dots)"/>
    <rect width="$W" height="$H" fill="url(#glow)"/>
    <rect x=".5" y=".5" width="$((W-1))" height="$((H-1))" rx="17.5" fill="none" stroke="#fff" stroke-opacity=".08"/>

    <text x="600" y="104" text-anchor="middle" class="sans in d1" font-size="68" font-weight="800" fill="#ececf1" letter-spacing="-1.5">Leonardo Anthony</text>
    <text x="600" y="152" text-anchor="middle" class="sans in d2" font-size="30" font-weight="600" fill="#f2774a">Dev full-stack &amp; Martech Engineer</text>

    <g class="in d3">
      <text x="370" y="230" text-anchor="middle" class="sans" font-size="48" font-weight="800" fill="#ececf1">5+</text>
      <text x="370" y="264" text-anchor="middle" class="mono" font-size="18" fill="#9a9aa6" letter-spacing="1">ANOS EM DEV</text>
      <line x1="485" y1="192" x2="485" y2="268" stroke="#fff" stroke-opacity=".1"/>
      <text x="600" y="230" text-anchor="middle" class="sans" font-size="48" font-weight="800" fill="#ececf1">23</text>
      <text x="600" y="264" text-anchor="middle" class="mono" font-size="18" fill="#9a9aa6" letter-spacing="1">PROJETOS NO AR</text>
      <line x1="715" y1="192" x2="715" y2="268" stroke="#fff" stroke-opacity=".1"/>
      <text x="830" y="230" text-anchor="middle" class="sans" font-size="48" font-weight="800" fill="#ececf1">8</text>
      <text x="830" y="264" text-anchor="middle" class="mono" font-size="18" fill="#9a9aa6" letter-spacing="1">SISTEMAS INTERNOS</text>
    </g>
  </g>
</svg>
EOF
echo "banner ok"
