document.addEventListener('DOMContentLoaded', () => {
    
    // Variabili di stato e costanti
    let isM63 = false;
    const a = 4;
    const b = 10;

    // Valori di default dei CFU, sovrascrivibili dall'utente tramite il pannello impostazioni
    const DEFAULT_CFU_TRIENNALE = 180;
    const DEFAULT_CFU_MAGISTRALE = 120;
    let numCfuTriennale = DEFAULT_CFU_TRIENNALE;
    let numCfuMagistrale = DEFAULT_CFU_MAGISTRALE;

    // Riferimenti agli elementi della UI (Viste e Testi)
    const selectionView = document.getElementById('selection-view');
    const calculatorView = document.getElementById('calculator-view');
    const calcTitle = document.getElementById('calc-title');
    const calcWarning = document.getElementById('calc-warning');
    const groupLodi12 = document.getElementById('group-lodi-12');

    // Riferimenti al pannello impostazioni CFU
    const btnSettings = document.getElementById('btn-settings');
    const settingsPanel = document.getElementById('settings-panel');
    const btnCloseSettings = document.getElementById('btn-close-settings');
    const inputCfuTriennale = document.getElementById('cfu-triennale');
    const inputCfuMagistrale = document.getElementById('cfu-magistrale');

    // Riferimenti agli elementi della UI (Righe risultati dinamiche)
    const rowMediaAgg = document.getElementById('row-media-agg');
    const rowBonusLodi = document.getElementById('row-bonus-lodi');
    const rowBonus100 = document.getElementById('row-bonus-100');

    // Riferimenti agli Input
    const inputMedia30 = document.getElementById('media_30');
    const inputLodi9 = document.getElementById('lodi_9');
    const inputLodi6 = document.getElementById('lodi_6');
    const inputLodi12 = document.getElementById('lodi_12');
    const inputFuoricorso = document.getElementById('fuoricorso');

    // Riferimenti agli Output
    const outMedia110 = document.getElementById('out-media-110');
    const outMediaAgg = document.getElementById('out-media-agg');
    const outBonusLodi = document.getElementById('out-bonus-lodi');
    const outBonusAnni = document.getElementById('out-bonus-anni');
    const outBonus100 = document.getElementById('out-bonus-100');
    const outFinale = document.getElementById('out-finale');

    // Configurazione degli Event Listeners sui bottoni
    document.getElementById('btn-triennale').addEventListener('click', () => setDegree(false));
    document.getElementById('btn-magistrale').addEventListener('click', () => setDegree(true));
    document.getElementById('btn-back').addEventListener('click', resetView);

    // Configurazione degli Event Listeners sugli input (per calcolo in tempo reale)
    const inputs = [inputMedia30, inputLodi9, inputLodi6, inputLodi12, inputFuoricorso];
    inputs.forEach(input => {
        input.addEventListener('input', calculate);
    });

    // Apertura/chiusura del pannello impostazioni CFU
    btnSettings.addEventListener('click', () => {
        settingsPanel.classList.toggle('hidden');
    });
    btnCloseSettings.addEventListener('click', () => {
        settingsPanel.classList.add('hidden');
    });

    // Aggiornamento dei CFU personalizzati (con salvataggio e ricalcolo immediato)
    inputCfuTriennale.addEventListener('input', () => {
        numCfuTriennale = parseInt(inputCfuTriennale.value) || DEFAULT_CFU_TRIENNALE;
        localStorage.setItem('cfuTriennale', numCfuTriennale);
        calculate();
    });
    inputCfuMagistrale.addEventListener('input', () => {
        numCfuMagistrale = parseInt(inputCfuMagistrale.value) || DEFAULT_CFU_MAGISTRALE;
        localStorage.setItem('cfuMagistrale', numCfuMagistrale);
        calculate();
    });

    // Al caricamento della pagina, recupero eventuali CFU personalizzati salvati in precedenza
    (function initCfuSettings() {
        const savedTriennale = localStorage.getItem('cfuTriennale');
        const savedMagistrale = localStorage.getItem('cfuMagistrale');

        if (savedTriennale) {
            numCfuTriennale = parseInt(savedTriennale) || DEFAULT_CFU_TRIENNALE;
            inputCfuTriennale.value = numCfuTriennale;
        }
        if (savedMagistrale) {
            numCfuMagistrale = parseInt(savedMagistrale) || DEFAULT_CFU_MAGISTRALE;
            inputCfuMagistrale.value = numCfuMagistrale;
        }
    })();

    // Funzione per impostare il tipo di laurea
    function setDegree(isMagistrale) {
        isM63 = isMagistrale;
        selectionView.classList.add('hidden');
        calculatorView.classList.remove('hidden');

        calcTitle.innerText = isM63 ? "Calcolatore Voto Laurea M63" : "Calcolatore Voto Laurea N46";
        calcWarning.innerText = isM63 
        ? "ATTENZIONE: Al punteggio va aggiunta la valutazione della commissione (0-4 punti)"
        : "ATTENZIONE: Al punteggio va aggiunta la valutazione della commissione (0-3 punti)";

        groupLodi12.style.display = isM63 ? 'flex' : 'none';
        rowMediaAgg.style.display = isM63 ? 'flex' : 'none';
        rowBonusLodi.style.display = isM63 ? 'none' : 'flex';
        rowBonus100.style.display = isM63 ? 'none' : 'flex';

        clearInputs();
    }

    // Funzione per tornare alla schermata iniziale
    function resetView() {
        calculatorView.classList.add('hidden');
        selectionView.classList.remove('hidden');
        clearInputs();
    }

    // Funzione per pulire i campi
    function clearInputs() {
        inputs.forEach(input => input.value = '');
        outMedia110.innerText = '0';
        outMediaAgg.innerText = '0';
        outBonusLodi.innerText = '0';
        outBonusAnni.innerText = '0';
        outBonus100.innerText = '0';
        outFinale.innerText = '0';
    }

    // Funzione principale di calcolo
    function calculate() {
        let media30 = parseFloat(inputMedia30.value) || 0;
        let lodi9 = parseInt(inputLodi9.value) || 0;
        let lodi6 = parseInt(inputLodi6.value) || 0;
        let rawFc = inputFuoricorso.value;
        let fc = rawFc === '' ? -1 : parseInt(rawFc);

        let media110 = media30 * (11 / 3);
        outMedia110.innerText = media110.toFixed(3);

        let votoFinale = 0;

        if (isM63) {
        let lodi12 = parseInt(inputLodi12.value) || 0;
        let aggLodi = ((lodi9 * 9) + (lodi6 * 6) + (lodi12 * 12)) / numCfuMagistrale;
        let mediaAgg = ((media30 + aggLodi) * a) - b;

        let bonusFc = 0;
        if (fc >= 0) {
            if (fc < 1) bonusFc = 4;
            else if (fc <= 1) bonusFc = 2.5;
            else if (fc <= 2) bonusFc = 1;
        }

        votoFinale = mediaAgg + bonusFc;
        outMediaAgg.innerText = mediaAgg.toFixed(3);
        outBonusAnni.innerText = bonusFc.toString();
        } else {
        let bonusLodi = (((lodi9 * 9) + (lodi6 * 6)) / numCfuTriennale) * (11 / 3);
        let bonusAnni = fc < 0 ? 0 : Math.max(4 - fc, 0);
        let bonus100 = media110 >= 100 ? 1 : 0;

        votoFinale = media110 + bonusLodi + bonusAnni + bonus100;
        outBonusLodi.innerText = bonusLodi.toFixed(3);
        outBonusAnni.innerText = bonusAnni.toFixed(3);
        outBonus100.innerText = bonus100.toString();
        }

        outFinale.innerText = votoFinale.toFixed(4);
    }
});
