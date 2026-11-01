# Ícones de serviço do leonardoanthony.dev (src/components/icons/service-icons.tsx), viewBox 24x24, traço.
# Função em vez de array associativo: o bash do macOS (3.2) não tem declare -A.
icon(){ case "$1" in
  site) echo '<rect x="3" y="4" width="18" height="13" rx="1.5"/><path d="M8 21h8M12 17v4M3 8h18"/>';;
  sistema) echo '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>';;
  automacao) echo '<circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="18" r="2"/><path d="M7 6h10M6 8l5 8M18 8l-5 8"/>';;
  integracao) echo '<path d="M9 3v4M15 3v4M7 7h10v4a5 5 0 0 1-10 0zM12 16v5"/>';;
  dashboard) echo '<path d="M3 21h18M6 17v-5M11 17V6M16 17v-3M21 17V9"/>';;
  crm) echo '<rect x="3" y="4" width="5" height="16" rx="1"/><rect x="10" y="4" width="5" height="11" rx="1"/><rect x="17" y="4" width="4" height="7" rx="1"/>';;
  ecommerce) echo '<path d="M3 4h2.2l2.1 10.1a1.6 1.6 0 0 0 1.6 1.3h8.3a1.6 1.6 0 0 0 1.6-1.2L21 8H6.1"/><circle cx="9.5" cy="19.5" r="1.3"/><circle cx="17" cy="19.5" r="1.3"/>';;
esac; }
