# Gerado por gerar_pagina.py a partir de painel.html. NAO EDITE A MAO.
PAGINA = r"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Atendimentos Tercerizado.</title>
<style>
  :root { --azul:#1f4e78; --azul2:#2e75b6; --verde:#1f7a54; --amarelo:#b8860b; --vermelho:#c0392b;
          --bg:#eef2f7; --card:#ffffff; --txt:#243447; --muted:#6b7a8d; --linha:#e3e9f0; }
  * { box-sizing:border-box; }
  body { margin:0; font-family:"Segoe UI",Roboto,Arial,sans-serif; background:var(--bg); color:var(--txt); }
  header { background:linear-gradient(120deg,#1f4e78,#2e75b6); color:#fff; padding:20px 24px; }
  header h1 { margin:0; font-size:22px; }
  header p { margin:4px 0 0; opacity:.85; font-size:13px; }
  .cab-topo { display:flex; align-items:center; gap:16px; flex-wrap:wrap; }
  .logo { height:56px; width:auto; background:#fff; padding:6px 10px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,.2); }
  .topbtns { margin-top:12px; display:flex; gap:8px; flex-wrap:wrap; }
  .topbtns button { border:0; border-radius:8px; padding:8px 12px; font-size:13px; cursor:pointer; background:rgba(255,255,255,.16); color:#fff; }
  .topbtns button:hover { background:rgba(255,255,255,.28); }
  .estados { padding:16px 24px 4px; }
  .estados .titulo { font-size:13px; color:var(--muted); margin-bottom:8px; font-weight:600; }
  .ufbtns { display:flex; gap:8px; flex-wrap:wrap; }
  .ufbtn { border:1px solid #cfd8e3; background:#fff; border-radius:10px; padding:8px 12px; cursor:pointer;
           font-size:14px; display:flex; align-items:center; gap:7px; transition:.12s; }
  .ufbtn:hover { border-color:var(--azul2); }
  .ufbtn.ativo { background:var(--azul); color:#fff; border-color:var(--azul); }
  .ufbtn .n { background:#eef2f7; color:var(--azul); border-radius:12px; padding:1px 8px; font-size:12px; font-weight:700; }
  .ufbtn.ativo .n { background:rgba(255,255,255,.25); color:#fff; }
  .busca-wrap { padding:12px 24px 0; display:flex; gap:8px; flex-wrap:wrap; align-items:center; }
  #busca { flex:1; min-width:220px; max-width:360px; padding:9px 12px; border:1px solid #cfd8e3; border-radius:8px; font-size:14px; }
  .busca-wrap select { padding:9px 12px; border:1px solid #cfd8e3; border-radius:8px; font-size:14px; background:#fff; max-width:260px; }
  .busca-wrap .sep { width:1px; height:26px; background:var(--linha); margin:0 4px; }
  .btn-filtro { border:1px solid #cfd8e3; background:#fff; border-radius:8px; padding:9px 12px; font-size:13px; cursor:pointer; }
  .btn-filtro:hover { background:#eef2f7; }
  .ms { position:relative; }
  .ms-btn { padding:9px 12px; border:1px solid #cfd8e3; border-radius:8px; background:#fff; font-size:14px; cursor:pointer; max-width:280px; text-align:left; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .ms-btn:hover { border-color:var(--azul2); }
  .ms-pop { display:none; position:absolute; z-index:15; top:calc(100% + 4px); left:0; background:#fff; border:1px solid #cfd8e3;
            border-radius:10px; box-shadow:0 6px 20px rgba(0,0,0,.15); width:300px; max-height:340px; overflow:auto; padding:8px; }
  .ms-pop.on { display:block; }
  .ms-acoes { font-size:12.5px; padding:4px 6px 8px; border-bottom:1px solid var(--linha); margin-bottom:6px; }
  .ms-acoes a { color:var(--azul2); cursor:pointer; }
  .ms-lista label { display:flex; align-items:center; gap:8px; padding:6px; font-size:13.5px; border-radius:6px; cursor:pointer; }
  .ms-lista label:hover { background:#eef5fd; }
  .ms-lista input { width:auto; margin:0; }
  .ms-lista .vazio { color:var(--muted); font-size:13px; padding:8px; }
  .conteudo { padding:16px 24px 40px; }
  .placeholder { padding:60px 20px; text-align:center; color:var(--muted); font-size:15px; }
  .estado-cab { display:flex; align-items:center; gap:12px; margin:8px 0 14px; flex-wrap:wrap; }
  .estado-cab h2 { margin:0; font-size:22px; color:var(--azul); }
  .estado-cab .sub { color:var(--muted); font-size:14px; }
  .secao-titulo { font-size:14px; font-weight:700; color:var(--txt); margin:18px 0 10px; display:flex;
                  align-items:center; gap:10px; border-left:4px solid var(--azul2); padding-left:8px; }
  .btn-add { border:0; border-radius:8px; padding:6px 12px; font-size:13px; cursor:pointer; background:var(--verde); color:#fff; }
  .btn-add:hover { filter:brightness(1.08); }
  .tec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(290px,1fr)); gap:12px; }
  .tec-card { background:#fff; border:1px solid var(--linha); border-radius:10px; padding:12px 14px 12px 44px;
              border-left:5px solid var(--verde); box-shadow:0 2px 6px rgba(30,60,90,.06); position:relative; cursor:grab; }
  .tec-card.dragging { opacity:.4; cursor:grabbing; }
  .tec-card.drop-antes { box-shadow:-4px 0 0 0 var(--azul2), 0 2px 6px rgba(30,60,90,.06); }
  .tec-card.drop-depois { box-shadow:4px 0 0 0 var(--azul2), 0 2px 6px rgba(30,60,90,.06); }
  .tec-card .tec-prio { position:absolute; left:10px; top:12px; width:24px; height:24px; border-radius:50%;
              background:var(--azul); color:#fff; font-size:12px; font-weight:700; display:flex;
              align-items:center; justify-content:center; box-shadow:0 1px 3px rgba(30,60,90,.25); }
  .tec-card .tec-drag { position:absolute; left:12px; bottom:12px; color:var(--muted); font-size:15px; cursor:grab; user-select:none; }
  .tec-card .nome { font-weight:700; font-size:15px; padding-right:60px; }
  .tec-card .valor { position:absolute; right:12px; top:12px; font-weight:700; color:var(--verde); }
  .tec-card .l { font-size:12.5px; color:var(--muted); margin-top:3px; }
  .tec-card .obs { font-size:12px; color:#7a6a3a; background:#fffaf0; border-radius:6px; padding:5px 8px; margin-top:6px; }
  .tec-card .acoes { margin-top:10px; display:flex; gap:8px; }
  .tec-card .acoes button { border:1px solid var(--linha); background:#f6f9fc; border-radius:6px; padding:4px 10px; font-size:12px; cursor:pointer; }
  .tec-card .acoes .del { color:var(--vermelho); }
  .tec-card .acoes button:hover { background:#eef2f7; }
  table { width:100%; border-collapse:collapse; background:#fff; border-radius:10px; overflow:hidden;
          box-shadow:0 2px 8px rgba(30,60,90,.07); font-size:13.5px; }
  thead th { background:var(--azul); color:#fff; text-align:left; padding:10px 12px; font-weight:600; }
  thead th.th-f { cursor:pointer; user-select:none; white-space:nowrap; }
  thead th.th-f:hover { background:var(--azul2); }
  thead th.th-f .fseta { opacity:.75; font-size:11px; margin-left:2px; }
  thead th.th-f.ativo { background:var(--verde); }
  thead th.th-f.ativo .fseta::after { content:" ●"; font-size:9px; }
  #colPop { position:fixed; }
  tbody td { padding:9px 12px; border-bottom:1px solid var(--linha); vertical-align:top; }
  tbody tr:nth-child(even){ background:#f6f9fc; }
  tbody tr:hover { background:#eef5fd; }
  .serie { font-weight:700; color:var(--azul); }
  .valor-unit { font-weight:700; color:var(--verde); white-space:nowrap; }
  .badge-dep { display:inline-block; background:#eef2f7; border-radius:6px; padding:1px 7px; font-size:11.5px; color:var(--muted); }
  .acoes-cel { white-space:nowrap; }
  .acoes-cel button { border:1px solid var(--linha); background:#f6f9fc; border-radius:6px; padding:3px 8px; font-size:12px; cursor:pointer; margin-right:4px; }
  .acoes-cel .del { color:var(--vermelho); }
  .acoes-cel button:hover { background:#eef2f7; }
  .overlay { position:fixed; inset:0; background:rgba(20,35,55,.55); display:none; align-items:center; justify-content:center; z-index:20; padding:16px; }
  .overlay.on { display:flex; }
  .modal { background:#fff; border-radius:14px; width:100%; max-width:520px; max-height:92vh; overflow:auto; box-shadow:0 10px 40px rgba(0,0,0,.3); }
  .modal h3 { margin:0; padding:18px 20px; background:linear-gradient(120deg,#1f4e78,#2e75b6); color:#fff; border-radius:14px 14px 0 0; font-size:17px; }
  .modal .corpo { padding:18px 20px; }
  .campo { margin-bottom:12px; }
  .campo label { display:block; font-size:12.5px; font-weight:600; color:var(--muted); margin-bottom:4px; }
  .campo input, .campo select, .campo textarea { width:100%; padding:9px 11px; border:1px solid #cfd8e3; border-radius:8px; font-size:14px; font-family:inherit; }
  .campo textarea { min-height:60px; resize:vertical; }
  .modal .rodape { padding:14px 20px; display:flex; justify-content:flex-end; gap:10px; border-top:1px solid var(--linha); }
  .modal .rodape button { border:0; border-radius:8px; padding:9px 16px; font-size:14px; cursor:pointer; }
  .modal .rodape .cancelar { background:#eef2f7; color:var(--txt); }
  .modal .rodape .salvar { background:var(--verde); color:#fff; }
  #status { position:fixed; bottom:16px; right:16px; background:#243447; color:#fff; padding:10px 16px; border-radius:8px;
            font-size:13px; opacity:0; transition:.2s; pointer-events:none; z-index:30; }
  #status.on { opacity:.95; }

  /* ---------- abas: Equipamentos | Chamados ---------- */
  .abas { display:flex; gap:4px; padding:0 24px; background:linear-gradient(120deg,#1f4e78,#2e75b6); }
  .aba { border:0; background:rgba(255,255,255,.12); color:#fff; font-size:14px; font-family:inherit;
         padding:10px 18px; border-radius:10px 10px 0 0; cursor:pointer; opacity:.8; }
  .aba:hover { background:rgba(255,255,255,.22); opacity:1; }
  .aba.ativa { background:var(--bg); color:var(--azul); font-weight:700; opacity:1; }
  .tela { display:none; }
  .tela.on { display:block; }

  /* ---------- chamados ---------- */
  .ch-resumo { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:10px; padding:16px 24px 0; }
  .ch-cartao { background:#fff; border:1px solid var(--linha); border-left:5px solid var(--azul2); border-radius:10px;
               padding:12px 14px; cursor:pointer; transition:.12s; box-shadow:0 2px 6px rgba(30,60,90,.06); }
  .ch-cartao:hover { border-color:var(--azul2); transform:translateY(-1px); }
  .ch-cartao.ativo { background:#eaf2fb; border-color:var(--azul2); box-shadow:0 0 0 2px var(--azul2) inset; }
  .ch-cartao .n { font-size:26px; font-weight:700; line-height:1.1; }
  .ch-cartao .r { font-size:12.5px; color:var(--muted); margin-top:2px; }

  .ch-barra { padding:14px 24px 0; display:flex; gap:8px; flex-wrap:wrap; align-items:center; }
  .ch-barra input[type=text], .ch-barra select { padding:9px 12px; border:1px solid #cfd8e3; border-radius:8px;
                                                 font-size:14px; background:#fff; font-family:inherit; }
  .ch-barra input[type=text] { flex:1; min-width:220px; max-width:340px; }

  .ch-tabela { width:100%; border-collapse:collapse; background:#fff; border:1px solid var(--linha);
               border-radius:10px; overflow:hidden; font-size:13.5px; }
  .ch-tabela th { background:#f5f8fc; text-align:left; padding:10px; font-size:12.5px; color:var(--muted);
                  border-bottom:1px solid var(--linha); white-space:nowrap; }
  .ch-tabela td { padding:9px 10px; border-bottom:1px solid var(--linha); vertical-align:top; }
  .ch-tabela tbody tr:hover { background:#f7fbff; }
  .ch-tabela tbody tr { cursor:pointer; }
  .ch-os { font-family:Consolas,monospace; font-weight:700; color:var(--azul); white-space:nowrap; }
  .ch-sub { color:var(--muted); font-size:12px; }

  .sit { display:inline-block; padding:3px 9px; border-radius:20px; font-size:12px; font-weight:600;
         color:#fff; white-space:nowrap; }
  .ch-dias { font-weight:700; white-space:nowrap; }
  .ch-dias.alerta { color:var(--amarelo); }
  .ch-dias.grave  { color:var(--vermelho); }
  .ch-dias.sem    { color:var(--muted); font-weight:400; font-style:italic; }
  .ch-acao { border:1px solid #cfd8e3; background:#fff; border-radius:6px; padding:3px 7px; cursor:pointer; font-size:13px; }
  .ch-acao:hover { background:#eef2f7; }

  .hist { border-top:1px solid var(--linha); margin-top:4px; padding-top:10px; }
  .hist-item { display:flex; gap:10px; padding:7px 0; border-bottom:1px dashed var(--linha); font-size:13px; }
  .hist-item:last-child { border-bottom:0; }
  .hist-em { color:var(--muted); font-size:12px; white-space:nowrap; min-width:112px; font-family:Consolas,monospace; }
  .campo2 { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
  .aviso-caixa { background:#fff8e6; border:1px solid #f0d99b; color:#7a5c00; border-radius:8px;
                 padding:10px 12px; font-size:13px; margin:14px 24px 0; }

  /* ---------- funil: quantos chamados em cada passo ---------- */
  .funil { display:flex; gap:6px; flex-wrap:wrap; padding:16px 24px 0; }
  .funil-p { background:#fff; border:1px solid var(--linha); border-left:4px solid #999; border-radius:9px;
             padding:7px 11px; cursor:pointer; font-size:12.5px; display:flex; align-items:center; gap:8px;
             transition:.12s; box-shadow:0 1px 4px rgba(30,60,90,.05); }
  .funil-p:hover { border-color:var(--azul2); transform:translateY(-1px); }
  .funil-p.ativo { background:#eaf2fb; box-shadow:0 0 0 2px var(--azul2) inset; }
  .funil-p .ord { background:#eef2f7; color:var(--muted); border-radius:50%; width:19px; height:19px;
                  display:inline-flex; align-items:center; justify-content:center; font-size:11px; font-weight:700; }
  .funil-p .qt { font-weight:700; font-size:15px; }
  .funil-seta { color:#c3ccd8; align-self:center; font-size:13px; }

  /* ---------- trilha dentro do chamado ---------- */
  .trilha { display:flex; flex-wrap:wrap; gap:4px; margin-bottom:6px; }
  .trilha-p { flex:1; min-width:64px; text-align:center; font-size:10.5px; padding:5px 3px; border-radius:6px;
              background:#eef2f7; color:var(--muted); line-height:1.25; }
  .trilha-p.feito  { background:#dff0e6; color:#1f7a54; }
  .trilha-p.agora  { background:var(--azul); color:#fff; font-weight:700; }
  .trilha-p .nq { display:block; font-size:9.5px; opacity:.75; }
  .trilha-cancel { background:#fde8e6; color:#c0392b; font-weight:700; padding:7px; border-radius:6px;
                   text-align:center; font-size:12px; margin-bottom:6px; }

  .passos-box { border:1px solid var(--linha); border-radius:10px; padding:12px 14px; background:#f8fbff; margin-top:4px; }
  .passos-box > label { font-size:13px; font-weight:700; color:var(--txt); display:block; margin-bottom:9px; }
  .btn-passo { display:block; width:100%; text-align:left; border:1px solid var(--azul2); background:var(--azul2);
               color:#fff; border-radius:9px; padding:11px 14px; font-size:13.5px; font-family:inherit;
               cursor:pointer; margin-bottom:7px; transition:.12s; }
  .btn-passo:hover { filter:brightness(1.1); }
  .btn-passo .seta { float:right; opacity:.8; }
  .btn-passo.secundario { background:#fff; color:var(--azul); }
  .btn-passo.perigo { background:#fff; color:var(--vermelho); border-color:#e8b4ae; }
  .passos-nota { font-size:12px; color:var(--muted); margin:2px 0 0; }

  .btn-avancar { display:block; width:100%; border:0; background:var(--verde); color:#fff; border-radius:10px;
                 padding:14px 16px; font-size:15px; font-weight:700; font-family:inherit; cursor:pointer; transition:.12s; }
  .btn-avancar:hover { filter:brightness(1.08); }
  .btn-avancar .prox { display:block; font-size:12.5px; font-weight:400; opacity:.9; margin-top:3px; }
  .link-cancelar { display:block; text-align:center; margin-top:10px; font-size:12.5px; color:var(--vermelho);
                   cursor:pointer; text-decoration:underline; background:none; border:0; font-family:inherit; width:100%; }
  .destinos label { display:flex; gap:10px; align-items:flex-start; padding:10px 12px; border:1px solid #cfd8e3;
                    border-radius:8px; margin-bottom:8px; cursor:pointer; font-size:14px; background:#fff; }
  .destinos label:hover { border-color:var(--azul2); }
  .destinos input { margin-top:3px; }
  .de-para { font-size:13.5px; color:var(--muted); margin:0 0 12px; }
  .de-para b { color:var(--txt); }
  .hist-quem { background:#eef2f7; color:var(--azul); border-radius:10px; padding:1px 8px; font-size:11.5px;
               font-weight:600; white-space:nowrap; }

  .ch-avancar { border:0; background:var(--verde); color:#fff; border-radius:7px; padding:6px 10px; cursor:pointer;
                font-size:12.5px; font-weight:600; font-family:inherit; white-space:nowrap; }
  .ch-avancar:hover { filter:brightness(1.08); }
  .ch-avancar.reabrir { background:#fff; color:var(--azul); border:1px solid #cfd8e3; font-weight:500; }
  .ch-acoes { display:flex; gap:6px; align-items:center; justify-content:flex-end; }
</style>
</head>
<body>
<header>
  <div class="cab-topo">
    <img src="/logo.jpg" alt="Solivetti" class="logo" onerror="this.style.display='none'">
    <div>
      <h1>Painel de Atendimentos por Estado</h1>
      <p>Escolha o estado para ver as séries e os clientes.</p>
    </div>
  </div>
  <div class="topbtns" id="btnsEquip">
    <button id="btnImportar">📥 Importar Excel (séries)</button>
    <button id="btnRestaurar">↺ Restaurar da planilha</button>
    <button id="btnAtualizar">🔄 Atualizar e salvar nas planilhas</button>
  </div>
  <div class="topbtns" id="btnsCham" style="display:none">
    <button id="btnNovoCham">➕ Novo chamado</button>
    <button id="btnImpCham">📥 Importar planilha de chamados</button>
  </div>
</header>
<nav class="abas">
  <button class="aba ativa" data-tela="telaEquip">🖨️ Equipamentos por estado</button>
  <button class="aba" data-tela="telaCham">🛠️ Chamados <span id="abaChamN"></span></button>
</nav>
<div class="tela on" id="telaEquip">
<div class="estados">
  <div class="titulo">ESCOLHA O ESTADO:</div>
  <div class="ufbtns" id="ufbtns"></div>
</div>
<div class="busca-wrap">
  <div class="ms" id="msCidade">
    <button type="button" class="ms-btn" id="msBtn">🏙️ Cidade: todas ▾</button>
    <div class="ms-pop" id="msPop">
      <div class="ms-acoes"><a id="msTodas">Marcar todas</a> &nbsp;·&nbsp; <a id="msLimpar">Limpar</a></div>
      <div class="ms-lista" id="msLista"></div>
    </div>
  </div>
  <input type="text" id="busca" placeholder="🔎 Buscar por série, cliente ou modelo...">
  <span class="sep"></span>
  <select id="fSalvos"><option value="">★ Filtros salvos</option></select>
  <button id="btnSalvarFiltro" class="btn-filtro">💾 Salvar filtro</button>
  <button id="btnExcluirFiltro" class="btn-filtro" title="Excluir o filtro salvo selecionado">🗑️</button>
</div>
<div class="ms-pop" id="colPop">
  <div class="ms-acoes"><a id="colLimpar">✖ Limpar filtro desta coluna</a></div>
  <div class="ms-lista" id="colLista"></div>
</div>
<div class="conteudo" id="conteudo"><div class="placeholder">Carregando...</div></div>
</div><!-- /telaEquip -->

<div class="tela" id="telaCham">
  <div class="funil" id="chFunil"></div>
  <div class="ch-resumo" id="chResumo"></div>
  <div class="ch-barra">
    <input type="text" id="chBusca" placeholder="🔎 Buscar por OS, cliente, parceiro, rastreio ou pedido...">
    <select id="chUF"><option value="">📍 Todos os estados</option></select>
    <select id="chParceiro"><option value="">🤝 Todos os parceiros</option></select>
    <select id="chSit"><option value="">◉ Todos os passos</option></select>
    <select id="chOrdem">
      <option value="dias">⏱️ Mais parados primeiro</option>
      <option value="os">Nº da OS</option>
      <option value="cliente">Cliente</option>
      <option value="parceiro">Parceiro</option>
    </select>
    <button class="btn-filtro" id="chLimpar">✖ Limpar filtros</button>
  </div>
  <div class="conteudo" id="chConteudo"><div class="placeholder">Carregando...</div></div>
</div><!-- /telaCham -->

<div class="overlay" id="ovTec"><div class="modal">
  <h3 id="tTitulo">Novo técnico</h3>
  <div class="corpo">
    <div class="campo"><label>Estado (UF) *</label><select id="tUF"></select></div>
    <div class="campo"><label>Nome do técnico / empresa *</label><input type="text" id="tNome"></div>
    <div class="campo"><label>CNPJ</label><input type="text" id="tCnpj" placeholder="00.000.000/0000-00"></div>
    <div class="campo"><label>Cidade / Local</label><input type="text" id="tLocal"></div>
    <div class="campo"><label>Valor</label><input type="text" id="tValor" placeholder="Ex.: R$ 150,00"></div>
    <div class="campo"><label>Telefone / WhatsApp</label><input type="text" id="tTelefone"></div>
    <div class="campo"><label>Contato</label><input type="text" id="tContato"></div>
    <div class="campo"><label>E-mail</label><input type="text" id="tEmail"></div>
    <div class="campo"><label>Observações</label><textarea id="tObs"></textarea></div>
  </div>
  <div class="rodape"><button class="cancelar" id="tCancelar">Cancelar</button><button class="salvar" id="tSalvar">Salvar</button></div>
</div></div>

<div class="overlay" id="ovEq"><div class="modal">
  <h3 id="eTitulo">Novo equipamento</h3>
  <div class="corpo">
    <div class="campo"><label>Estado (UF) *</label><select id="eUF"></select></div>
    <div class="campo"><label>Série *</label><input type="text" id="eSerie"></div>
    <div class="campo"><label>Cliente</label><input type="text" id="eCliente"></div>
    <div class="campo"><label>Cidade</label><input type="text" id="eCidade"></div>
    <div class="campo"><label>Fabricante</label><input type="text" id="eFabricante"></div>
    <div class="campo"><label>Modelo</label><input type="text" id="eModelo"></div>
    <div class="campo"><label>Departamento</label><input type="text" id="eDepartamento"></div>
    <div class="campo"><label>Valor unitário</label><input type="text" id="eValorUnit" placeholder="Ex.: R$ 1.200,00"></div>
  </div>
  <div class="rodape"><button class="cancelar" id="eCancelar">Cancelar</button><button class="salvar" id="eSalvar">Salvar</button></div>
</div></div>

<div class="overlay" id="ovImp"><div class="modal">
  <h3>📥 Importar equipamentos (Excel)</h3>
  <div class="corpo">
    <div class="campo"><label>Arquivo (.xls ou .xlsx)</label><input type="file" id="impFile" accept=".xls,.xlsx"></div>
    <div class="campo"><label>Como atualizar?</label>
      <label style="font-weight:400;display:block;margin-bottom:6px"><input type="radio" name="impModo" value="sincronizar" checked> <b>Sincronizar (recomendado)</b> — a série é única: se ela aparecer em outro estado, cidade ou cliente, sai de onde estava e vai para o lugar do arquivo. O que não vier no arquivo é removido.</label>
      <label style="font-weight:400;display:block;margin-bottom:6px"><input type="radio" name="impModo" value="substituir"> <b>Substituir</b> toda a lista de equipamentos pelos do arquivo</label>
      <label style="font-weight:400;display:block"><input type="radio" name="impModo" value="merge"> Apenas <b>adicionar novas</b> séries e <b>atualizar</b> as existentes (não remove nada)</label>
    </div>
    <div style="font-size:12.5px;color:var(--muted)">O arquivo deve ter, na primeira linha, colunas com <b>Série</b>, Cliente, Cidade, UF, Modelo, Fabricante e Departamento (a ordem não importa). Os <b>técnicos não são afetados</b>.</div>
  </div>
  <div class="rodape"><button class="cancelar" id="impCancelar">Cancelar</button><button class="salvar" id="impImportar">Importar</button></div>
</div></div>

<div class="overlay" id="ovImpRes"><div class="modal" style="max-width:760px">
  <h3>📋 Resultado da importação</h3>
  <div class="corpo" id="impResCorpo"></div>
  <div class="rodape"><button class="salvar" id="impResFechar">Fechar</button></div>
</div></div>

<div class="overlay" id="ovCham"><div class="modal" style="max-width:720px">
  <h3 id="cTitulo">Novo chamado</h3>
  <div class="corpo">
    <div id="cTrilha"></div>
    <div class="campo"><label>Nº da O.S. *</label><input type="text" id="cOS"></div>
    <div class="campo"><label>Cliente *</label><input type="text" id="cCliente" list="listaClientes">
      <datalist id="listaClientes"></datalist></div>
    <div class="campo2">
      <div class="campo"><label>Cidade</label><input type="text" id="cCidade"></div>
      <div class="campo"><label>Estado (UF)</label><select id="cUF"></select></div>
    </div>
    <div class="campo"><label>Parceiro / terceirizado</label><input type="text" id="cParceiro" list="listaParceiros">
      <datalist id="listaParceiros"></datalist></div>
    <div class="campo2">
      <div class="campo"><label>Aberto em</label><input type="date" id="cAberto"></div>
      <div class="campo"><label>Pedido de compra</label><input type="text" id="cPedido"></div>
    </div>
    <div class="campo"><label>Código de rastreio</label><input type="text" id="cRastreio"></div>
    <div class="campo"><label>Observação</label><textarea id="cObs"></textarea></div>
    <div class="passos-box" id="cPassos"></div>
    <div id="cHist"></div>
  </div>
  <div class="rodape">
    <button class="cancelar" id="cExcluir" style="margin-right:auto;background:#fde8e6;color:#c0392b;display:none">🗑️ Excluir</button>
    <button class="cancelar" id="cCancelar">Cancelar</button>
    <button class="salvar" id="cSalvar">Salvar</button>
  </div>
</div></div>

<div class="overlay" id="ovImpCh"><div class="modal">
  <h3>Importar chamados da planilha</h3>
  <div class="corpo">
    <div class="campo"><label>Arquivo .xlsx com a aba "CHAMADOS TERCEIRIZADOS"</label>
      <input type="file" id="impChFile" accept=".xlsx"></div>
    <div class="campo"><label>O que fazer com os que já estão aqui</label>
      <select id="impChModo">
        <option value="merge">Só acrescentar os que faltam (recomendado)</option>
        <option value="substituir">Apagar tudo e pôr os da planilha</option>
      </select></div>
    <p style="font-size:13px;color:var(--muted);margin:4px 0 0">
      No modo <b>acrescentar</b>, chamado cujo nº de O.S. já existe aqui é ignorado — o que você
      atualizou no painel nunca é sobrescrito. A planilha não tem data de abertura, então os
      importados entram <b>sem data</b> e aparecem como "sem data" na coluna de dias.</p>
  </div>
  <div class="rodape"><button class="cancelar" id="impChCancelar">Cancelar</button>
    <button class="salvar" id="impChImportar">Importar</button></div>
</div></div>

<div class="overlay" id="ovPasso"><div class="modal" style="max-width:560px">
  <h3 id="pTitulo">Registrar andamento</h3>
  <div class="corpo">
    <p class="de-para" id="pDePara"></p>
    <div class="destinos" id="pDestinos"></div>
    <div class="campo" id="pCampoRastreio" style="display:none"><label>Código de rastreio *</label>
      <input type="text" id="pRastreio" placeholder="Ex.: AD123456789BR"></div>
    <div class="campo"><label>Seu nome *</label><input type="text" id="pNome" placeholder="Quem está registrando"></div>
    <div class="campo"><label>O que foi feito *</label>
      <textarea id="pTexto" placeholder="Ex.: liguei para o cliente, confirmou que a impressora voltou a imprimir"></textarea></div>
  </div>
  <div class="rodape"><button class="cancelar" id="pCancelar">Voltar</button>
    <button class="salvar" id="pConfirmar">Confirmar</button></div>
</div></div>

<div id="status"></div>

<script>
const UFS_BR = ["AC","AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT","PA","PB","PE","PI","PR","RJ","RN","RO","RR","RS","SC","SE","SP","TO"];
let TEC = {}, EQUIP = [], FILTROS = [], ufAtual = "";
const $ = id => document.getElementById(id);
function esc(t){ return (t||"").toString().replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }
function aviso(msg){ const s=$('status'); s.textContent=msg; s.classList.add('on'); setTimeout(()=>s.classList.remove('on'),1800); }

const elBtns=$('ufbtns'), elConteudo=$('conteudo'), busca=$('busca'), fSalvos=$('fSalvos');
let cidadesSel = new Set();   // cidades marcadas (vazio = todas)
let filtroCol = { serie:new Set(), cliente:new Set(), equip:new Set() };  // filtros por coluna (vazio = todos)
// extrai o valor de cada coluna filtrável de um equipamento
const COLVAL = { serie:d=>d.serie||'', cliente:d=>d.cliente||'', cidade:d=>d.cidade||'',
                 equip:d=>((d.fabricante||'')+' '+(d.modelo||'')).trim() };
// devolve o Set de seleção da coluna (cidade compartilha o filtro de cidade do topo)
function selCol(k){ return k==='cidade' ? cidadesSel : filtroCol[k]; }

async function carregar(){
  const r = await fetch('/api/dados'); const d = await r.json();
  TEC = d.tecnicos||{}; EQUIP = d.equipamentos||[]; FILTROS = d.filtros||[];
  CHAM = d.chamados||[]; if(d._situacoes) SITS = d._situacoes;
  if(d._trilha) TRILHA = d._trilha;
  if(d._exige) EXIGE = d._exige;
}
async function api(url, body){
  try {
    const r = await fetch(url, {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(body)});
    if(!r.ok) throw new Error('http '+r.status);
    const d = await r.json();
    if(d.erro) throw new Error(d.erro);
    TEC = d.tecnicos||{}; EQUIP = d.equipamentos||[]; FILTROS = d.filtros||[]; CHAM = d.chamados||CHAM;
    aviso('✔ Salvo no servidor');
    return true;
  } catch(e){ alert('Não consegui salvar no servidor. Verifique se o Painel.bat continua aberto.\\n\\n'+e); return false; }
}
function contarUF(){ const c={}; EQUIP.forEach(e=>{ c[e.uf]=(c[e.uf]||0)+1; }); return c; }

function construirBotoes(){
  const contUF = contarUF();
  const ufs = [...new Set([...UFS_BR, ...Object.keys(contUF), ...Object.keys(TEC)])].sort();
  elBtns.innerHTML='';
  ufs.forEach(uf => {
    const b=document.createElement('div');
    b.className='ufbtn'+(uf===ufAtual?' ativo':''); b.dataset.uf=uf;
    b.innerHTML=`${esc(uf)} <span class="n">${contUF[uf]||0}</span>`;
    b.onclick=()=>{ selecionarUF(uf); };
    elBtns.appendChild(b);
  });
}

function selecionarUF(uf){ ufAtual=uf; busca.value=''; cidadesSel=new Set(); filtroCol={serie:new Set(),cliente:new Set(),equip:new Set()}; construirBotoes(); popularCidades(); render(); }

function cidadesDoEstado(){
  return [...new Set(EQUIP.filter(d=>d.uf===ufAtual).map(d=>d.cidade).filter(Boolean))].sort();
}
function popularCidades(){
  const cidades=cidadesDoEstado();
  $('msLista').innerHTML = cidades.length
    ? cidades.map(c=>`<label><input type="checkbox" value="${esc(c)}" ${cidadesSel.has(c)?'checked':''}> ${esc(c)}</label>`).join('')
    : '<div class="vazio">Nenhuma cidade neste estado.</div>';
  $('msLista').querySelectorAll('input').forEach(chk=>{
    chk.onchange=()=>{ chk.checked ? cidadesSel.add(chk.value) : cidadesSel.delete(chk.value); atualizarBtnCidade(); render(); };
  });
  atualizarBtnCidade();
}
function atualizarBtnCidade(){
  const n=cidadesSel.size;
  $('msBtn').textContent = n===0 ? '🏙️ Cidade: todas ▾' : (n===1 ? '🏙️ '+[...cidadesSel][0]+' ▾' : `🏙️ ${n} cidades ▾`);
}

function popularFiltrosSalvos(){
  fSalvos.innerHTML='<option value="">★ Filtros salvos</option>'+FILTROS.map(f=>`<option value="${f.id}">${esc(f.nome)}</option>`).join('');
}

function render(){
  if(!ufAtual){ elConteudo.innerHTML=`<div class="placeholder">👆 Selecione um estado acima.</div>`; return; }
  const q=busca.value.trim().toLowerCase();
  let itens=EQUIP.filter(d=>d.uf===ufAtual);
  if(cidadesSel.size) itens=itens.filter(d=>cidadesSel.has(d.cidade));
  if(filtroCol.serie.size)   itens=itens.filter(d=>filtroCol.serie.has(COLVAL.serie(d)));
  if(filtroCol.cliente.size) itens=itens.filter(d=>filtroCol.cliente.has(COLVAL.cliente(d)));
  if(filtroCol.equip.size)   itens=itens.filter(d=>filtroCol.equip.has(COLVAL.equip(d)));
  if(q) itens=itens.filter(d=>[d.serie,d.cliente,d.cidade,d.modelo].join(' ').toLowerCase().includes(q));
  const tecnicos=TEC[ufAtual]||[];
  let rosterHTML;
  if(tecnicos.length===0){
    rosterHTML=`<div class="placeholder" style="padding:24px;color:var(--vermelho)">⚠️ Nenhum técnico cadastrado para ${esc(ufAtual)}. Clique em “Adicionar técnico”.</div>`;
  } else {
    rosterHTML=`<div class="tec-grid" id="tecGrid">`+tecnicos.map((t,i)=>`
      <div class="tec-card" draggable="true" data-id="${t.id}">
        <span class="tec-prio">${i+1}º</span>
        <span class="valor">${t.valor?esc(t.valor):'—'}</span>
        <div class="nome">${esc(t.nome)}</div>
        ${t.cnpj?`<div class="l">🏢 ${esc(t.cnpj)}</div>`:''}
        ${t.local?`<div class="l">📍 ${esc(t.local)}</div>`:''}
        ${t.telefone?`<div class="l">📞 ${esc(t.telefone)}</div>`:''}
        ${t.contato?`<div class="l">👤 ${esc(t.contato)}</div>`:''}
        ${t.email?`<div class="l">✉️ ${esc(t.email)}</div>`:''}
        ${t.obs?`<div class="obs">${esc(t.obs)}</div>`:''}
        <span class="tec-drag" title="Arraste para reordenar a prioridade">⠿</span>
        <div class="acoes">
          <button onclick="editarTec('${esc(ufAtual)}','${t.id}')">✏️ Editar</button>
          <button class="del" onclick="excluirTec('${esc(ufAtual)}','${t.id}')">🗑️ Excluir</button>
        </div>
      </div>`).join('')+`</div>`;
  }
  let tabelaHTML;
  if(itens.length===0){
    tabelaHTML=`<div class="placeholder">Nenhum equipamento neste estado.</div>`;
  } else {
    const linhas=itens.map(d=>`
      <tr>
        <td class="serie">${esc(d.serie)}</td>
        <td>${esc(d.cliente)}</td>
        <td>${esc(d.cidade)}</td>
        <td>${esc(d.fabricante)} ${esc(d.modelo)}${d.departamento?` <span class="badge-dep">${esc(d.departamento)}</span>`:''}</td>
        <td class="valor-unit">${d.valorUnit?esc(d.valorUnit):'—'}</td>
        <td class="acoes-cel"><button onclick="editarEquip('${d.id}')">✏️</button><button class="del" onclick="excluirEquip('${d.id}')">🗑️</button></td>
      </tr>`).join('');
    const thF=(k,t)=>`<th class="th-f${selCol(k).size?' ativo':''}" onclick="abrirColPop(event,'${k}')">${t} <span class="fseta">▾</span></th>`;
    tabelaHTML=`<table><thead><tr>${thF('serie','Série')}${thF('cliente','Cliente')}${thF('cidade','Cidade')}${thF('equip','Equipamento')}<th>Valor unit.</th><th>Ações</th></tr></thead><tbody>${linhas}</tbody></table>`;
  }
  elConteudo.innerHTML=`
    <div class="estado-cab"><h2>${esc(ufAtual)}</h2>
      <span class="sub">${itens.length} equipamento(s) &nbsp;•&nbsp; ${tecnicos.length} técnico(s)</span></div>
    <div class="secao-titulo">🛠️ Técnicos de ${esc(ufAtual)}
      <button class="btn-add" onclick="novoTec()">➕ Adicionar técnico</button></div>
    ${rosterHTML}
    <div class="secao-titulo">📋 Equipamentos e clientes em ${esc(ufAtual)}
      <button class="btn-add" onclick="novoEquip()">➕ Adicionar equipamento</button></div>
    ${tabelaHTML}`;
}

// ---- Arrastar e soltar: prioridade dos técnicos ----
let dragTecId=null;
function limparDrop(){ elConteudo.querySelectorAll('.drop-antes,.drop-depois').forEach(c=>c.classList.remove('drop-antes','drop-depois')); }
elConteudo.addEventListener('dragstart',e=>{ const card=e.target.closest('.tec-card'); if(!card) return;
  dragTecId=card.dataset.id; card.classList.add('dragging');
  if(e.dataTransfer){ e.dataTransfer.effectAllowed='move'; e.dataTransfer.setData('text/plain',dragTecId); } });
elConteudo.addEventListener('dragend',e=>{ const card=e.target.closest('.tec-card'); if(card) card.classList.remove('dragging'); limparDrop(); dragTecId=null; });
elConteudo.addEventListener('dragover',e=>{ if(!dragTecId) return; const card=e.target.closest('.tec-card');
  if(!card||card.dataset.id===dragTecId) return; e.preventDefault();
  if(e.dataTransfer) e.dataTransfer.dropEffect='move'; limparDrop();
  const r=card.getBoundingClientRect(); const antes=e.clientX < r.left + r.width/2;
  card.classList.add(antes?'drop-antes':'drop-depois'); });
elConteudo.addEventListener('drop',async e=>{ if(!dragTecId) return; const card=e.target.closest('.tec-card');
  limparDrop(); if(!card){ dragTecId=null; return; } e.preventDefault();
  const alvoId=card.dataset.id; if(alvoId===dragTecId){ dragTecId=null; return; }
  const r=card.getBoundingClientRect(); const antes=e.clientX < r.left + r.width/2;
  const lista=(TEC[ufAtual]||[]).map(t=>t.id); const from=lista.indexOf(dragTecId);
  if(from<0){ dragTecId=null; return; } lista.splice(from,1);
  let to=lista.indexOf(alvoId); if(!antes) to+=1; lista.splice(to,0,dragTecId);
  dragTecId=null;
  if(await api('/api/tecnico',{op:'reorder',uf:ufAtual,ordem:lista})) render(); });

// ---- Modal técnico ----
const ovTec=$('ovTec');
UFS_BR.forEach(u=>$('tUF').insertAdjacentHTML('beforeend',`<option>${u}</option>`));
let tEditId=null, tEditUF=null;
function abrirTec(t){ $('tTitulo').textContent=t; ovTec.classList.add('on'); $('tNome').focus(); }
window.novoTec=function(){ tEditId=null; tEditUF=null; $('tUF').value=ufAtual||'SP';
  ['tNome','tCnpj','tLocal','tValor','tTelefone','tContato','tEmail','tObs'].forEach(i=>$(i).value=''); abrirTec('Novo técnico'); };
window.editarTec=function(uf,id){ const t=(TEC[uf]||[]).find(x=>x.id===id); if(!t) return;
  tEditId=id; tEditUF=uf; $('tUF').value=uf; $('tNome').value=t.nome||''; $('tCnpj').value=t.cnpj||''; $('tLocal').value=t.local||'';
  $('tValor').value=t.valor||''; $('tTelefone').value=t.telefone||''; $('tContato').value=t.contato||'';
  $('tEmail').value=t.email||''; $('tObs').value=t.obs||''; abrirTec('Editar técnico'); };
window.excluirTec=async function(uf,id){ const t=(TEC[uf]||[]).find(x=>x.id===id);
  if(!confirm('Excluir o técnico "'+(t?t.nome:'')+'"?')) return;
  if(await api('/api/tecnico',{op:'delete',id})){ construirBotoes(); render(); } };
$('tSalvar').onclick=async function(){
  const uf=$('tUF').value; if(!$('tNome').value.trim()){ alert('Informe o nome do técnico.'); return; }
  const item={ nome:$('tNome').value.trim(), cnpj:$('tCnpj').value.trim(), local:$('tLocal').value.trim(), valor:$('tValor').value.trim(),
    telefone:$('tTelefone').value.trim(), contato:$('tContato').value.trim(), email:$('tEmail').value.trim(), obs:$('tObs').value.trim() };
  const ok = tEditId ? await api('/api/tecnico',{op:'update',uf,id:tEditId,item}) : await api('/api/tecnico',{op:'add',uf,item});
  if(ok){ ovTec.classList.remove('on'); ufAtual=uf; construirBotoes(); render(); } };
$('tCancelar').onclick=()=>ovTec.classList.remove('on');
ovTec.onclick=e=>{ if(e.target===ovTec) ovTec.classList.remove('on'); };

// ---- Modal equipamento ----
const ovEq=$('ovEq');
UFS_BR.forEach(u=>$('eUF').insertAdjacentHTML('beforeend',`<option>${u}</option>`));
let eEditId=null;
function abrirEq(t){ $('eTitulo').textContent=t; ovEq.classList.add('on'); $('eSerie').focus(); }
window.novoEquip=function(){ eEditId=null; $('eUF').value=ufAtual||'SP';
  ['eSerie','eCliente','eCidade','eFabricante','eModelo','eDepartamento','eValorUnit'].forEach(i=>$(i).value=''); abrirEq('Novo equipamento'); };
window.editarEquip=function(id){ const d=EQUIP.find(x=>x.id===id); if(!d) return;
  eEditId=id; $('eUF').value=d.uf; $('eSerie').value=d.serie||''; $('eCliente').value=d.cliente||'';
  $('eCidade').value=d.cidade||''; $('eFabricante').value=d.fabricante||''; $('eModelo').value=d.modelo||''; $('eDepartamento').value=d.departamento||''; $('eValorUnit').value=d.valorUnit||''; abrirEq('Editar equipamento'); };
window.excluirEquip=async function(id){ const d=EQUIP.find(x=>x.id===id);
  if(!confirm('Excluir o equipamento de série "'+(d?d.serie:'')+'"?')) return;
  if(await api('/api/equip',{op:'delete',id})){ construirBotoes(); render(); } };
$('eSalvar').onclick=async function(){
  if(!$('eSerie').value.trim()){ alert('Informe a série do equipamento.'); return; }
  const item={ uf:$('eUF').value, serie:$('eSerie').value.trim(), cliente:$('eCliente').value.trim(),
    cidade:$('eCidade').value.trim(), fabricante:$('eFabricante').value.trim(), modelo:$('eModelo').value.trim(), departamento:$('eDepartamento').value.trim(), valorUnit:$('eValorUnit').value.trim() };
  const ok = eEditId ? await api('/api/equip',{op:'update',id:eEditId,item}) : await api('/api/equip',{op:'add',item});
  if(ok){ ovEq.classList.remove('on'); ufAtual=item.uf; construirBotoes(); render(); } };
$('eCancelar').onclick=()=>ovEq.classList.remove('on');
ovEq.onclick=e=>{ if(e.target===ovEq) ovEq.classList.remove('on'); };

// ---- Restaurar / atualizar ----
$('btnRestaurar').onclick=async function(){
  if(!confirm('Isso descarta TODAS as inclusões/edições (técnicos e equipamentos) e volta aos dados originais da planilha. Continuar?')) return;
  if(await api('/api/restaurar',{})){ construirBotoes(); render(); } };
$('btnAtualizar').onclick=async function(){
  aviso('💾 Salvando nas planilhas...');
  try {
    const r=await fetch('/api/exportar',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'});
    if(!r.ok) throw new Error('http '+r.status);
    const d=await r.json();
    if(d.erro) throw new Error(d.erro);
    TEC=d.tecnicos||{}; EQUIP=d.equipamentos||[]; FILTROS=d.filtros||[];
    const ex=d._export||{};
    construirBotoes(); if(ufAtual) popularCidades(); render();
    aviso(`✔ Salvo: ${ex.equipamentos} equip. e ${ex.tecnicos} téc. nas planilhas`);
  } catch(e){ alert('Erro ao salvar nas planilhas:\\n'+e); }
};

// ---- Importar Excel ----
const ovImp=$('ovImp');
$('btnImportar').onclick=()=>{ $('impFile').value=''; ovImp.classList.add('on'); };
$('impCancelar').onclick=()=>ovImp.classList.remove('on');
ovImp.onclick=e=>{ if(e.target===ovImp) ovImp.classList.remove('on'); };
$('impImportar').onclick=async ()=>{
  const f=$('impFile').files[0];
  if(!f){ alert('Escolha um arquivo Excel (.xls ou .xlsx).'); return; }
  const modo=document.querySelector('input[name=impModo]:checked').value;
  if(modo==='substituir' && !confirm('Isso vai SUBSTITUIR toda a lista atual de equipamentos pelos do arquivo. Continuar?')) return;
  if(modo==='sincronizar' && !confirm('O arquivo passa a mandar: séries que estiverem em outro estado/cidade/cliente serão MOVIDAS, e as que não vierem no arquivo serão REMOVIDAS. Continuar?')) return;
  ovImp.classList.remove('on');
  const b64=await new Promise((res,rej)=>{ const fr=new FileReader(); fr.onload=()=>res(fr.result.split(',')[1]); fr.onerror=rej; fr.readAsDataURL(f); });
  try {
    const r=await fetch('/api/importar',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({nome:f.name,dados_b64:b64,modo})});
    if(!r.ok) throw new Error('http '+r.status);
    const d=await r.json();
    if(d.erro) throw new Error(d.erro);
    TEC=d.tecnicos||{}; EQUIP=d.equipamentos||[]; FILTROS=d.filtros||[];
    const s=d._import||{};
    construirBotoes(); popularCidades(); render();
    if(s.modo==='sincronizar'){ mostrarResultadoSinc(s); }
    else if(s.modo==='substituir'){ alert(`✔ Importado! ${s.importados} equipamento(s) na lista (substituiu ${s.removidos}).`); }
    else { alert(`✔ Importado! ${s.adicionados} novo(s) e ${s.atualizados} atualizado(s).`); }
  } catch(e){ alert('Erro ao importar o arquivo:\\n'+e); }
};

// ---- Resultado da sincronização ----
const ovImpRes=$('ovImpRes');
$('impResFechar').onclick=()=>ovImpRes.classList.remove('on');
ovImpRes.onclick=e=>{ if(e.target===ovImpRes) ovImpRes.classList.remove('on'); };
function lugarTxt(l){ return [l.uf,l.cidade,l.cliente].filter(v=>v).join(' · '); }
function blocoLista(titulo,cor,itens,total,linha){
  if(!total) return '';
  const extra = total>itens.length ? `<div style="font-size:12px;color:var(--muted);padding:6px 0">… e mais ${total-itens.length}. A lista completa está no painel.</div>` : '';
  const linhas = itens.map(linha).join('');
  return `<div style="margin-top:14px">
    <div style="font-weight:600;color:${cor};margin-bottom:6px">${titulo} (${total})</div>
    <div style="max-height:220px;overflow:auto;border:1px solid var(--linha);border-radius:8px">
      <table style="width:100%;border-collapse:collapse;font-size:12.5px">${linhas}</table></div>${extra}</div>`;
}
function mostrarResultadoSinc(s){
  const td='style="padding:5px 8px;border-bottom:1px solid var(--linha)"';
  let h=`<div style="font-size:14px">A série é única, então o arquivo mandou onde cada uma fica.</div>
    <div style="margin-top:10px;font-size:14px">
      <b>${s.total}</b> equipamento(s) no painel agora ·
      <b>${s.inalterados}</b> sem mudança ·
      <b>${s.movidos_total}</b> movido(s) ·
      <b>${s.novos_total}</b> novo(s) ·
      <b>${s.removidos_total}</b> removido(s)
    </div>`;
  if(s.duplicadas_no_arquivo) h+=`<div style="margin-top:8px;font-size:12.5px;color:var(--amarelo)">⚠ ${s.duplicadas_no_arquivo} série(s) apareceram mais de uma vez no arquivo; valeu a última linha de cada.</div>`;
  h+=blocoLista('Movidas de lugar','var(--azul)',s.movidos,s.movidos_total,
      m=>`<tr><td ${td}><b>${m.serie}</b></td><td ${td}>${lugarTxt(m.de)}</td><td ${td} align="center">→</td><td ${td}>${lugarTxt(m.para)}</td></tr>`);
  h+=blocoLista('Entraram no painel','var(--verde)',s.novos,s.novos_total,
      n=>`<tr><td ${td}><b>${n.serie}</b></td><td ${td}>${lugarTxt(n)}</td></tr>`);
  h+=blocoLista('Saíram do painel (não vieram no arquivo)','var(--vermelho)',s.removidos,s.removidos_total,
      r=>`<tr><td ${td}><b>${r.serie}</b></td><td ${td}>${lugarTxt(r)}</td></tr>`);
  $('impResCorpo').innerHTML=h;
  ovImpRes.classList.add('on');
}

// ---- Multi-seleção de cidade ----
const msCidade=$('msCidade'), msPop=$('msPop');
$('msBtn').onclick=(e)=>{ e.stopPropagation(); msPop.classList.toggle('on'); };
document.addEventListener('click', e=>{ if(!msCidade.contains(e.target)) msPop.classList.remove('on'); });
$('msTodas').onclick=()=>{ cidadesSel=new Set(cidadesDoEstado()); popularCidades(); render(); };
$('msLimpar').onclick=()=>{ cidadesSel=new Set(); popularCidades(); render(); };

// ---- Filtro por coluna (estilo Excel) ----
const colPop=$('colPop'); let colAtual=null;
function distintosCol(k){ return [...new Set(EQUIP.filter(d=>d.uf===ufAtual).map(d=>COLVAL[k](d)).filter(v=>v!==''))].sort((a,b)=>a.localeCompare(b,'pt')); }
window.abrirColPop=function(ev,k){
  ev.stopPropagation();
  if(colPop.classList.contains('on') && colAtual===k){ colPop.classList.remove('on'); return; }  // clicar de novo fecha
  colAtual=k;
  const sel=selCol(k), vals=distintosCol(k), todos=sel.size===0;
  $('colLista').innerHTML = vals.length
    ? vals.map(v=>`<label><input type="checkbox" value="${esc(v)}" ${todos||sel.has(v)?'checked':''}> ${esc(v)}</label>`).join('')
    : '<div class="vazio">Nada para filtrar nesta coluna.</div>';
  $('colLista').querySelectorAll('input').forEach(chk=>{ chk.onchange=aplicarCol; });
  const r=ev.currentTarget.getBoundingClientRect();
  colPop.style.left=Math.max(8, Math.min(r.left, window.innerWidth-320))+'px';
  colPop.style.top=(r.bottom+4)+'px';
  colPop.classList.add('on');
};
function aplicarCol(){
  const vals=distintosCol(colAtual);
  const marc=[...$('colLista').querySelectorAll('input')].filter(c=>c.checked).map(c=>c.value);
  const novo = marc.length===vals.length ? new Set() : new Set(marc);   // todos marcados = sem filtro
  if(colAtual==='cidade'){ cidadesSel=novo; popularCidades(); } else { filtroCol[colAtual]=novo; }
  render();
}
$('colLimpar').onclick=()=>{ if(colAtual==='cidade'){ cidadesSel=new Set(); popularCidades(); } else { filtroCol[colAtual]=new Set(); } colPop.classList.remove('on'); render(); };
document.addEventListener('click', e=>{ if(!colPop.contains(e.target) && !e.target.closest('.th-f')) colPop.classList.remove('on'); });

// ---- Filtros salvos ----
$('btnSalvarFiltro').onclick=async ()=>{
  if(!ufAtual){ alert('Escolha um estado antes de salvar o filtro.'); return; }
  const rot = cidadesSel.size===1 ? ' - '+[...cidadesSel][0] : (cidadesSel.size>1 ? ` - ${cidadesSel.size} cidades` : '');
  const nome=(prompt('Nome para este filtro salvo:', ufAtual+rot)||'').trim();
  if(!nome) return;
  const item={ nome, uf:ufAtual, cidades:[...cidadesSel], busca:busca.value.trim() };
  if(await api('/api/filtro',{op:'add',item})){ popularFiltrosSalvos(); aviso('★ Filtro salvo'); }
};
$('btnExcluirFiltro').onclick=async ()=>{
  const id=fSalvos.value;
  if(!id){ alert('Selecione um filtro salvo na lista para excluir.'); return; }
  const f=FILTROS.find(x=>x.id===id);
  if(!confirm('Excluir o filtro salvo "'+(f?f.nome:'')+'"?')) return;
  if(await api('/api/filtro',{op:'delete',id})){ popularFiltrosSalvos(); }
};
fSalvos.addEventListener('change', ()=>{
  const f=FILTROS.find(x=>x.id===fSalvos.value);
  if(!f) return;
  ufAtual=f.uf; construirBotoes();
  filtroCol={serie:new Set(),cliente:new Set(),equip:new Set()};
  cidadesSel=new Set(f.cidades || (f.cidade?[f.cidade]:[]));   // compat: filtro antigo tinha 1 cidade
  popularCidades(); busca.value=f.busca||'';
  render();
});


/* =========================================================================
   CHAMADOS TERCEIRIZADOS
   Substitui a aba CHAMADOS da planilha do Google. O que ela nao tinha e aqui
   tem: data de abertura, contador de dias parado, situacao de lista fixa e
   historico (cada andamento vira uma linha, em vez de apagar o anterior).
   ========================================================================= */
let CHAM = [], SITS = [], TRILHA = [], EXIGE = {}, chFiltro = { busca:'', uf:'', parceiro:'', sit:'', atalho:'' }, chOrdem = 'dias';
const sitInfo = k => SITS.find(s => s.chave === k) || { rotulo:k||'?', cor:'#6b7a90', aberta:true };
const ehAberta = k => !!sitInfo(k).aberta;

function hojeISO(){ const d=new Date(); return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'); }
function diasParado(c){
  if(!c.aberto_em) return null;
  const ini = new Date(c.aberto_em + 'T00:00:00');
  if(isNaN(ini)) return null;
  const fim = c.fechado_em ? new Date(c.fechado_em + 'T00:00:00') : new Date();
  return Math.max(0, Math.round((fim - ini) / 86400000));
}
function dataBR(iso){
  if(!iso) return '';
  const p = String(iso).slice(0,10).split('-');
  return p.length===3 ? p[2]+'/'+p[1]+'/'+p[0] : iso;
}

/* ---- abas ---- */
document.querySelectorAll('.aba').forEach(b => b.onclick = () => {
  document.querySelectorAll('.aba').forEach(x => x.classList.remove('ativa'));
  document.querySelectorAll('.tela').forEach(x => x.classList.remove('on'));
  b.classList.add('ativa');
  $(b.dataset.tela).classList.add('on');
  const ehCham = b.dataset.tela === 'telaCham';
  $('btnsEquip').style.display = ehCham ? 'none' : '';
  $('btnsCham').style.display  = ehCham ? '' : 'none';
  if(ehCham) renderCham();
});

/* ---- filtros ---- */
function chListaBase(){
  let L = CHAM.slice();
  const a = chFiltro.atalho;
  if(a === 'abertos')   L = L.filter(c => ehAberta(c.situacao));
  if(a === 'parados')   L = L.filter(c => ehAberta(c.situacao) && (diasParado(c) ?? -1) > 15);
  if(a === 'semdata')   L = L.filter(c => ehAberta(c.situacao) && !c.aberto_em);
  if(a === 'encerrado') L = L.filter(c => !ehAberta(c.situacao));
  if(chFiltro.uf === '__sem')      L = L.filter(c => !c.uf);
  else if(chFiltro.uf)             L = L.filter(c => (c.uf||'') === chFiltro.uf);
  if(chFiltro.parceiro) L = L.filter(c => (c.parceiro||'') === chFiltro.parceiro);
  if(chFiltro.sit)      L = L.filter(c => c.situacao === chFiltro.sit);
  const q = chFiltro.busca.trim().toLowerCase();
  if(q) L = L.filter(c => [c.os,c.cliente,c.parceiro,c.rastreio,c.pedido,c.cidade,c.obs].join(' ').toLowerCase().includes(q));
  return L;
}
function chOrdenar(L){
  const f = {
    dias:     (a,b) => (diasParado(b) ?? -1) - (diasParado(a) ?? -1),
    os:       (a,b) => String(a.os).localeCompare(String(b.os), 'pt-BR', {numeric:true}),
    cliente:  (a,b) => String(a.cliente||'').localeCompare(String(b.cliente||''), 'pt-BR'),
    parceiro: (a,b) => String(a.parceiro||'').localeCompare(String(b.parceiro||''), 'pt-BR'),
  }[chOrdem];
  // Em aberto sempre antes dos fechados: o que precisa de acao fica no topo.
  return L.sort((a,b) => (ehAberta(b.situacao) - ehAberta(a.situacao)) || f(a,b));
}

function renderFunil(){
  // Quantos chamados parados em cada passo. E o retrato do processo:
  // onde a fila esta crescendo, aparece aqui.
  const cont = {};
  CHAM.forEach(c => { cont[c.situacao] = (cont[c.situacao]||0) + 1; });
  const passos = TRILHA.map(k => ({k:k, i:sitInfo(k)}));
  if(cont['cancelado']) passos.push({k:'cancelado', i:sitInfo('cancelado')});
  $('chFunil').innerHTML = passos.map((p, n) =>
    (n > 0 && p.k !== 'cancelado' ? '<span class="funil-seta">\u203a</span>' : '') +
    '<div class="funil-p' + (chFiltro.sit===p.k?' ativo':'') + '" data-k="' + p.k + '" ' +
    'style="border-left-color:' + p.i.cor + '" title="' + esc(p.i.rotulo) + '">' +
    (p.k === 'cancelado' ? '' : '<span class="ord">' + (n+1) + '</span>') +
    '<span>' + esc(p.i.rotulo) + '</span>' +
    '<span class="qt" style="color:' + p.i.cor + '">' + (cont[p.k]||0) + '</span></div>').join('');
  $('chFunil').querySelectorAll('.funil-p').forEach(el => el.onclick = () => {
    chFiltro.sit = (chFiltro.sit === el.dataset.k) ? '' : el.dataset.k;
    chFiltro.atalho = '';
    renderCham();
  });
}

function renderResumo(){
  const ab = CHAM.filter(c => ehAberta(c.situacao));
  const cartoes = [
    { k:'abertos', n:ab.length,                                        r:'em andamento',         cor:'var(--azul2)' },
    { k:'parados', n:ab.filter(c => (diasParado(c) ?? -1) > 15).length, r:'parados +15 dias',     cor:'var(--vermelho)' },
    { k:'semdata', n:ab.filter(c => !c.aberto_em).length,               r:'sem data de abertura', cor:'var(--muted)' },
    { k:'encerrado', n:CHAM.length - ab.length,                         r:'encerrados',           cor:'var(--verde)' },
  ];
  $('chResumo').innerHTML = cartoes.map(c =>
    '<div class="ch-cartao' + (chFiltro.atalho===c.k?' ativo':'') + '" data-k="' + c.k + '" style="border-left-color:' + c.cor + '">' +
    '<div class="n" style="color:' + c.cor + '">' + c.n + '</div><div class="r">' + c.r + '</div></div>').join('');
  $('chResumo').querySelectorAll('.ch-cartao').forEach(el => el.onclick = () => {
    chFiltro.atalho = (chFiltro.atalho === el.dataset.k) ? '' : el.dataset.k;
    renderCham();
  });
  $('abaChamN').textContent = ab.length ? '(' + ab.length + ')' : '';
}

function popularSelects(){
  const sel = (id, itens, atual) => {
    const e = $(id), prim = e.options[0].outerHTML;
    e.innerHTML = prim + itens.map(i =>
      '<option value="' + esc(i.v) + '"' + (atual===i.v?' selected':'') + '>' + esc(i.t) + '</option>').join('');
  };
  const ufs = [...new Set(CHAM.map(c => c.uf).filter(Boolean))].sort();
  sel('chUF', ufs.map(u => ({v:u, t:u})), chFiltro.uf);
  if(CHAM.some(c => !c.uf)) $('chUF').insertAdjacentHTML('beforeend',
    '<option value="__sem"' + (chFiltro.uf==='__sem'?' selected':'') + '>\u2014 sem estado \u2014</option>');
  const ps = [...new Set(CHAM.map(c => c.parceiro).filter(Boolean))].sort();
  sel('chParceiro', ps.map(x => ({v:x, t:x})), chFiltro.parceiro);
  sel('chSit', SITS.map(s => ({v:s.chave, t:(s.passo ? s.passo + '. ' : '') + s.rotulo})), chFiltro.sit);
  $('listaClientes').innerHTML  = [...new Set(CHAM.map(c=>c.cliente).filter(Boolean))].sort()
                                    .map(x=>'<option value="' + esc(x) + '">').join('');
  $('listaParceiros').innerHTML = ps.map(x=>'<option value="' + esc(x) + '">').join('');
}

function renderCham(){
  renderFunil();
  renderResumo();
  popularSelects();
  const L = chOrdenar(chListaBase());

  const semUF = CHAM.filter(c => ehAberta(c.situacao) && !c.uf).length;
  const alerta = semUF ? '<div class="aviso-caixa">\u26a0\ufe0f ' + semUF + ' chamado(s) em aberto est\u00e3o <b>sem estado</b>. ' +
      'A planilha antiga n\u00e3o tinha coluna de cidade \u2014 o estado foi deduzido do nome do cliente e nesses n\u00e3o deu. ' +
      'Abra o chamado e preencha para ele aparecer nos filtros por estado.</div>' : '';

  if(!L.length){
    $('chConteudo').innerHTML = alerta + '<div class="placeholder">Nenhum chamado com esses filtros.</div>';
    return;
  }
  const linhas = L.map(c => {
    const si = sitInfo(c.situacao), d = diasParado(c), ab = ehAberta(c.situacao);
    let cls = 'sem', txt = 'sem data';
    if(d !== null){ txt = d + (d === 1 ? ' dia' : ' dias'); cls = (ab && d > 30) ? 'grave' : (ab && d > 15) ? 'alerta' : ''; }
    return '<tr data-id="' + c.id + '">' +
      '<td class="ch-os">' + esc(c.os) + '</td>' +
      '<td>' + esc(c.cliente) + (c.obs ? '<div class="ch-sub">' + esc(c.obs.slice(0,70)) + (c.obs.length>70?'\u2026':'') + '</div>' : '') + '</td>' +
      '<td>' + esc(c.cidade||'') + (c.uf ? ' <b>' + esc(c.uf) + '</b>' : '<span class="ch-sub">\u2014</span>') + '</td>' +
      '<td>' + esc(c.parceiro||'\u2014') + '</td>' +
      '<td><span class="sit" style="background:' + si.cor + '">' +
        (si.passo ? si.passo + '. ' : '') + esc(si.rotulo) + '</span></td>' +
      '<td>' + (dataBR(c.aberto_em) || '<span class="ch-sub">\u2014</span>') + '</td>' +
      '<td class="ch-dias ' + cls + '">' + txt + '</td>' +
      '<td>' + esc(c.rastreio||'') + '</td>' +
      '<td>' + esc(c.pedido||'') + '</td>' +
      '<td><div class="ch-acoes">' + botaoAvancarHTML(c) +
        '<button class="ch-acao" title="Corrigir dados do chamado">\u270f\ufe0f</button></div></td></tr>';
  }).join('');
  $('chConteudo').innerHTML = alerta +
    '<div class="estado-cab"><h2>Chamados</h2><span class="sub">' + L.length + ' de ' + CHAM.length + ' chamado(s)</span></div>' +
    '<table class="ch-tabela"><thead><tr>' +
    '<th>O.S.</th><th>Cliente</th><th>Cidade / UF</th><th>Parceiro</th><th>Passo do fluxo</th>' +
    '<th>Aberto em</th><th>Parado h\u00e1</th><th>Rastreio</th><th>Pedido</th><th></th>' +
    '</tr></thead><tbody>' + linhas + '</tbody></table>';
  $('chConteudo').querySelectorAll('tbody tr').forEach(tr =>
    tr.onclick = () => abrirCham(tr.dataset.id));
  // O Avancar da linha abre a caixa direto, sem passar pelo chamado.
  $('chConteudo').querySelectorAll('.ch-avancar').forEach(b => b.onclick = e => {
    e.stopPropagation();
    const c = CHAM.find(x => x.id === b.dataset.id);
    if(!c) return;
    cEditId = c.id;
    abrirPasso(c, (sitInfo(c.situacao).proximos || []).filter(x => x.para !== 'cancelado'));
  });
}

/* ---- modal ---- */
const ovCham = $('ovCham');
let cEditId = null;
UFS_BR.forEach(u => $('cUF').insertAdjacentHTML('beforeend', '<option>' + u + '</option>'));

function trilhaHTML(c){
  const atual = c.situacao;
  if(atual === 'cancelado'){
    return '<div class="trilha-cancel">\u26d4 Chamado cancelado</div>';
  }
  const pos = TRILHA.indexOf(atual);
  return '<div class="trilha">' + TRILHA.map((k, i) => {
    const cls = i < pos ? 'feito' : (i === pos ? 'agora' : '');
    return '<div class="trilha-p ' + cls + '" title="' + esc(sitInfo(k).rotulo) + '">' +
           '<span class="nq">' + (i+1) + '</span>' + esc(sitInfo(k).rotulo) + '</div>';
  }).join('') + '</div>';
}

function histHTML(c){
  const h = (c.historico || []);
  if(!h.length) return '';
  return '<div class="hist"><label style="font-size:13px;font-weight:600;color:var(--muted)">📜 Histórico</label>' +
    h.slice().reverse().map(x =>
      '<div class="hist-item"><span class="hist-em">' + esc(x.em) + '</span>' +
      (x.quem && x.quem !== 'painel' ? '<span class="hist-quem">' + esc(x.quem) + '</span>' : '') +
      '<span>' + esc(x.texto) + '</span></div>').join('') +
    '</div>';
}

function passosHTML(c){
  // Um botao so. Para onde ele leva, e o que foi feito, a pessoa diz na
  // caixa que abre em seguida. Quem decide se pode e o servidor.
  const ps = (sitInfo(c.situacao).proximos || []).filter(x => x.para !== 'cancelado');
  const podeCancelar = (sitInfo(c.situacao).proximos || []).some(x => x.para === 'cancelado');
  let html = '';
  if(!ps.length){
    html = '<p class="passos-nota">Este chamado chegou ao fim do fluxo.</p>';
  } else {
    const reabrir = ps.length === 1 && ps[0].para === TRILHA[0] && !ehAberta(c.situacao);
    const titulo = reabrir ? 'Reabrir chamado' : 'Avan\u00e7ar para a pr\u00f3xima etapa \u2192';
    const sub = ps.length === 1 ? sitInfo(ps[0].para).rotulo : 'a caixa pergunta qual caminho';
    html = '<button type="button" class="btn-avancar" id="btnAvancar">' + titulo +
           '<span class="prox">' + esc(sub) + '</span></button>';
  }
  if(podeCancelar) html += '<button type="button" class="link-cancelar" id="btnCancelarCh">cancelar este chamado</button>';
  return html;
}

function botaoAvancarHTML(c){
  const ps = (sitInfo(c.situacao).proximos || []).filter(x => x.para !== 'cancelado');
  if(!ps.length) return '';
  if(!ehAberta(c.situacao))
    return '<button class="ch-avancar reabrir" data-id="' + c.id + '" title="Reabrir chamado">Reabrir</button>';
  const prox = ps.length === 1 ? sitInfo(ps[0].para).rotulo : 'escolher caminho';
  return '<button class="ch-avancar" data-id="' + c.id + '" title="Pr\u00f3ximo: ' + esc(prox) + '">Avan\u00e7ar \u2192</button>';
}

/* ---- caixa de andamento: para onde, quem, o que fez ---- */
const ovPasso = $('ovPasso');
let pDestinos = [];
function nomeLembrado(){ try { return localStorage.getItem('painel_nome') || ''; } catch(e){ return ''; } }
function lembrarNome(n){ try { localStorage.setItem('painel_nome', n); } catch(e){} }

function abrirPasso(c, destinos){
  pDestinos = destinos;
  const de = sitInfo(c.situacao).rotulo;
  if(destinos.length === 1){
    const d = destinos[0];
    $('pTitulo').textContent = d.para === 'cancelado' ? 'Cancelar chamado' : 'Registrar andamento';
    $('pDePara').innerHTML = 'O.S. <b>' + esc(c.os) + '</b> \u2014 de <b>' + esc(de) + '</b> para <b>' + esc(sitInfo(d.para).rotulo) + '</b>';
    $('pDestinos').innerHTML = '';
  } else {
    $('pTitulo').textContent = 'Registrar andamento';
    $('pDePara').innerHTML = 'O.S. <b>' + esc(c.os) + '</b> est\u00e1 em <b>' + esc(de) + '</b>. O que aconteceu?';
    $('pDestinos').innerHTML = destinos.map((d, i) =>
      '<label><input type="radio" name="pDest" value="' + d.para + '"' + (i===0?' checked':'') + '>' +
      '<span>' + esc(d.rotulo) + '<br><small style="color:var(--muted)">vai para: ' + esc(sitInfo(d.para).rotulo) + '</small></span></label>').join('');
  }
  $('pRastreio').value = c.rastreio || '';
  const atualizaExigencia = () => {
    const para = destinos.length === 1 ? destinos[0].para
               : (document.querySelector('input[name=pDest]:checked') || {}).value;
    $('pCampoRastreio').style.display = EXIGE[para] === 'rastreio' ? '' : 'none';
  };
  $('pDestinos').querySelectorAll('input').forEach(r => r.onchange = atualizaExigencia);
  atualizaExigencia();
  $('pNome').value = nomeLembrado();
  $('pTexto').value = '';
  ovPasso.classList.add('on');
  ($('pNome').value ? $('pTexto') : $('pNome')).focus();
}
$('pCancelar').onclick = () => ovPasso.classList.remove('on');
ovPasso.onclick = e => { if(e.target === ovPasso) ovPasso.classList.remove('on'); };
$('pConfirmar').onclick = async () => {
  const c = CHAM.find(x => x.id === cEditId);
  if(!c) return;
  const nome = $('pNome').value.trim(), texto = $('pTexto').value.trim();
  if(!nome){ alert('Diga quem est\u00e1 registrando.'); $('pNome').focus(); return; }
  if(!texto){ alert('Descreva o que foi feito.'); $('pTexto').focus(); return; }
  let para = pDestinos.length === 1 ? pDestinos[0].para
           : (document.querySelector('input[name=pDest]:checked') || {}).value;
  if(!para){ alert('Escolha o que aconteceu.'); return; }
  const rastreio = $('pRastreio').value.trim();
  if(EXIGE[para] === 'rastreio' && !rastreio){
    alert('Para marcar \u00abPe\u00e7a enviada\u00bb informe o c\u00f3digo de rastreio.'); $('pRastreio').focus(); return;
  }
  const base = ovCham.classList.contains('on')
    ? camposDoForm()
    : { os:c.os, cliente:c.cliente, cidade:c.cidade, uf:c.uf, parceiro:c.parceiro,
        aberto_em:c.aberto_em, pedido:c.pedido, rastreio:c.rastreio, obs:c.obs };
  const item = Object.assign(base, {situacao: para});
  if(EXIGE[para] === 'rastreio') item.rastreio = rastreio;
  if(!item.os){ alert('Informe o n\u00famero da O.S.'); return; }
  if(!item.cliente){ alert('Informe o cliente.'); return; }
  lembrarNome(nome);
  if(await api('/api/chamado', {op:'update', id:cEditId, item:item, nota:texto, quem:nome})){
    aviso('\u2714 ' + sitInfo(para).rotulo);
    ovPasso.classList.remove('on'); ovCham.classList.remove('on');
    renderCham();
  }
};

window.abrirCham = function(id){
  const c = CHAM.find(x => x.id === id);
  if(!c) return;
  cEditId = id;
  $('cTitulo').textContent = 'Chamado O.S. ' + (c.os || '');
  $('cTrilha').innerHTML = trilhaHTML(c);
  $('cOS').value = c.os || ''; $('cCliente').value = c.cliente || '';
  $('cCidade').value = c.cidade || ''; $('cUF').value = c.uf || '';
  $('cParceiro').value = c.parceiro || '';
  $('cAberto').value = (c.aberto_em || '').slice(0,10);
  $('cPedido').value = c.pedido || ''; $('cRastreio').value = c.rastreio || '';
  $('cObs').value = c.obs || '';
  $('cHist').innerHTML = histHTML(c);
  $('cPassos').style.display = ''; $('cPassos').innerHTML = passosHTML(c);
  const ps = (sitInfo(c.situacao).proximos || []);
  const bA = $('btnAvancar'), bC = $('btnCancelarCh');
  if(bA) bA.onclick = () => abrirPasso(c, ps.filter(x => x.para !== 'cancelado'));
  if(bC) bC.onclick = () => abrirPasso(c, ps.filter(x => x.para === 'cancelado'));
  $('cExcluir').style.display = '';
  ovCham.classList.add('on');
};

function camposDoForm(){
  return {
    os: $('cOS').value.trim(), cliente: $('cCliente').value.trim(),
    cidade: $('cCidade').value.trim(), uf: $('cUF').value,
    parceiro: $('cParceiro').value.trim(),
    aberto_em: $('cAberto').value, pedido: $('cPedido').value.trim(),
    rastreio: $('cRastreio').value.trim(), obs: $('cObs').value.trim(),
  };
}

$('btnNovoCham').onclick = () => {
  cEditId = null;
  $('cTitulo').textContent = 'Novo chamado';
  ['cOS','cCliente','cCidade','cParceiro','cPedido','cRastreio','cObs'].forEach(i => $(i).value = '');
  $('cUF').value = '';
  $('cAberto').value = hojeISO();          // chamado novo ja nasce com data
  // Todo chamado comeca no passo 1: nao se cria no meio do processo.
  $('cTrilha').innerHTML = trilhaHTML({situacao: TRILHA[0]});
  $('cPassos').style.display = 'none';
  $('cHist').innerHTML = ''; $('cExcluir').style.display = 'none';
  ovCham.classList.add('on'); $('cOS').focus();
};
$('cCancelar').onclick = () => ovCham.classList.remove('on');
ovCham.onclick = e => { if(e.target === ovCham) ovCham.classList.remove('on'); };

$('cSalvar').onclick = async () => {
  const item = camposDoForm();
  if(!item.os){ alert('Informe o n\u00famero da O.S.'); $('cOS').focus(); return; }
  if(!item.cliente){ alert('Informe o cliente.'); $('cCliente').focus(); return; }
  // Salvar grava os dados e a observacao; quem muda de passo sao os botoes.
  const body = cEditId
    ? { op:'update', id:cEditId, item:item }
    : { op:'add', item:item };
  if(await api('/api/chamado', body)){ ovCham.classList.remove('on'); renderCham(); }
};

$('cExcluir').onclick = async () => {
  if(!cEditId) return;
  const c = CHAM.find(x => x.id === cEditId);
  if(!confirm('Excluir o chamado da O.S. ' + (c ? c.os : '') + '?\nO hist\u00f3rico dele some junto.')) return;
  if(await api('/api/chamado', {op:'delete', id:cEditId})){ ovCham.classList.remove('on'); renderCham(); }
};

/* ---- filtros da barra ---- */
$('chBusca').addEventListener('input', e => { chFiltro.busca = e.target.value; renderCham(); });
$('chUF').addEventListener('change',   e => { chFiltro.uf = e.target.value; renderCham(); });
$('chParceiro').addEventListener('change', e => { chFiltro.parceiro = e.target.value; renderCham(); });
$('chSit').addEventListener('change',  e => { chFiltro.sit = e.target.value; renderCham(); });
$('chOrdem').addEventListener('change',e => { chOrdem = e.target.value; renderCham(); });
$('chLimpar').onclick = () => {
  chFiltro = { busca:'', uf:'', parceiro:'', sit:'', atalho:'' };
  $('chBusca').value = ''; $('chUF').value = ''; $('chParceiro').value = ''; $('chSit').value = '';
  renderCham();
};

/* ---- importar a planilha ---- */
const ovImpCh = $('ovImpCh');
$('btnImpCham').onclick = () => { $('impChFile').value = ''; ovImpCh.classList.add('on'); };
$('impChCancelar').onclick = () => ovImpCh.classList.remove('on');
$('impChImportar').onclick = async () => {
  const f = $('impChFile').files[0];
  if(!f){ alert('Escolha o arquivo .xlsx.'); return; }
  const modo = $('impChModo').value;
  if(modo === 'substituir' && !confirm('Isso APAGA os ' + CHAM.length + ' chamados que est\u00e3o aqui, com o hist\u00f3rico, e p\u00f5e os da planilha no lugar.\n\nConfirma?')) return;
  const b64 = await new Promise(ok => { const r = new FileReader();
    r.onload = () => ok(r.result.split(',')[1]); r.readAsDataURL(f); });
  const r = await fetch('/api/importar_chamados', {method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({nome:f.name, dados_b64:b64, modo:modo})});
  const d = await r.json();
  if(d.erro){ alert('N\u00e3o consegui importar:\n\n' + d.erro); return; }
  CHAM = d.chamados || [];
  ovImpCh.classList.remove('on');
  const i = d._impch || {};
  alert('Importa\u00e7\u00e3o conclu\u00edda.\n\n' +
        'Lidos na planilha: ' + (i.lidos||0) + '\n' +
        'Entraram no painel: ' + (i.importados||0) + '\n' +
        'Ignorados (O.S. j\u00e1 existia aqui): ' + (i.ignorados||0) + '\n' +
        'Sem estado definido: ' + (i.sem_uf||0));
  renderCham();
};

busca.addEventListener('input', render);
(async function(){ await carregar(); construirBotoes(); popularFiltrosSalvos(); render(); renderResumo(); })();
</script>
</body>
</html>
"""
