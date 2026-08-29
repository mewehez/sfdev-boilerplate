! Le Stop hook tourne après chaque tour. Sur un graphe de quelques centaines de fichiers c'est imperceptible, mais si tu passes le cap du millier, retire-le du Stop et garde SessionStart seul.



1. Installation

Le chemin recommandé est la marketplace officielle : /plugin install superpowers@claude-plugins-official. L'alternative communautaire : /plugin marketplace add obra/superpowers-marketplace puis /plugin install superpowers@superpowers-marketplace. Même plugin dans les deux cas.

! Superpowers charge par défaut un logo distant qui transmet sa version ; SUPERPOWERS_DISABLE_TELEMETRY le désactive. À poser dans l'environnement du projet. 
GitHub

! Superpowers injecte du contexte au SessionStart, comme notre hook. Deux injections cohabitent — d'où la règle de budget ci-dessous. 
GitHub