var POSTAG = {
    entity_types: []
}

var tags = [
    {
        "subtags": ['N', 'Np', 'Nc', 'Nb', 'Nu', 'Ny'],
        "color": "#b4bbff"
    },
    {
        "subtags": ['P'],
        "color": "#6ec1e2"
    },
    {
        "subtags": ['V'],
        "color": "#adf6a2"
    },
    {
        "subtags": ['A', 'Ab'],
        "color": "#f98fff"
    },
    {
        "subtags": ['M'],
        "color": "#fc6"
    },
    {
        "subtags": ['C', 'Cc', 'R', 'L', 'E', 'T', 'X'],
        "color": "#cc9"
    },
    {
        "subtags": ['CH'],
        "color": "#aaa"
    }
]

tags.forEach(tag => {
    var color = tag.color;
    var subtags = tag.subtags;
    subtags.forEach(subtag => {
        var entity = {
            type: subtag,
            labels: [subtag],
            bgColor: color,
            borderColor: 'darken'
        };
        POSTAG.entity_types.push(entity);
    })
})

var CHUNK = {
    entity_types: []
}

// B-AP, B-MP, B-NP, B-PP, B-QP, B-TP, B-VP, B-WH, B-WP, B-XP, I-AP, I-MP, I-NP, I-PP, I-QP, I-VP, I-WH , I-WP, I-XP, N-NP, O
var tags = [
    {
        "subtags": ['B-AP', 'I-AP'],
        "color": "#f98fff"
    },
    {
        "subtags": ['B-MP', 'I-MP'],
        "color": "#fc6"
    },
    {
        "subtags": ['B-NP', 'I-NP'],
        "color": "#b4bbff"
    },
    {
        "subtags": ['B-PP', 'I-PP'],
        "color": "#6ec1e2"
    },
    {
        "subtags": ['B-QP', 'I-QP'],
        "color": "#b4bbff"
    },
    {
        "subtags": ['B-TP', 'I-TP'],
        "color": "#b4bbff"
    },
    {
        "subtags": ['B-VP', 'I-VP'],
        "color": "#adf6a2"
    },
    {
        "subtags": ['B-WH', 'I-WH'],
        "color": "#adf6a2"
    },
    {
        "subtags": ['B-WP', 'I-WP'],
        "color": "#adf6a2"
    },
    {
        "subtags": ['B-XP', 'I-XP'],
        "color": "#cc9"
    },
    {
        "subtags": ['O'],
        "color": "#aaa"
    }
]

tags.forEach(tag => {
    var color = tag.color;
    var subtags = tag.subtags;
    subtags.forEach(subtag => {
        var entity = {
            type: subtag,
            labels: [subtag],
            bgColor: color,
            borderColor: 'darken'
        };
        CHUNK.entity_types.push(entity);
    })
})

var NER = {
    entity_types: []
}

var tags = [
    {
        "subtags": ['B-PER', 'I-PER'],
        "color": "#f96c62"
    },
    {
        "subtags": ["B-LOC", "I-LOC"],
        "color": "#17AFC1"
    },
    {
        "subtags": ["B-ORG", "I-ORG"],
        "color": "#1792C1"
    }
]

tags.forEach(tag => {
    var color = tag.color;
    var subtags = tag.subtags;
    subtags.forEach(subtag => {
        var entity = {
            type: subtag,
            labels: [subtag],
            bgColor: color,
            borderColor: 'darken'
        };
        NER.entity_types.push(entity);
    })
})

WS = {
    entity_types: [
        {
            type: '',
            labels: ['_'],
            bgColor: '#00B0FF',
            borderColor: 'darken'
        }
    ]
};