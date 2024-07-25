console.log('Hello')

const ctx = document.getElementById('candiChart');
const ctx1 = document.getElementById('partyChart');


var candiGraphData = {
    type: 'bar',
    data: {
    labels: [],
    datasets: [{
        label: '# of Votes',
        data: [],
        borderWidth: 1,
        
    }]
    },
    options: {}
}

var partyGraphData = {
    type: 'doughnut',
    data: {
    labels: [],
    datasets: [{
        data: [],
        borderWidth: 1,
        backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)',
            'rgb(128,128,128)'
        ],
        weight: 270,
        hoverOffset: 4
    }]
    },
    options: {
        rotation: 270,
        circumference: 180,
        cutout: '70%'
    }
}

var candiChart = new Chart(ctx, candiGraphData);
var partyChart = new Chart(ctx1, partyGraphData);

var socket = new WebSocket('ws://localhost:8000/ws/chart/');
socket.onmessage = function(e){
    var candiData = JSON.parse(e.data);

    // graphData.data.datasets[0].data = [
    //     candiData.trump,
    //     candiData.harris,
    //     candiData.joe,
    //     candiData.obama,
    //     candiData.mike,
    //     candiData.kennedy,
    //     candiData.west,
    //     candiData.oliver,
    //     candiData.halley,
    //     candiData.no
    // ];

    //Candiates
    var labels = Object.keys(candiData);
    var data = Object.values(candiData);

    candiGraphData.data.labels = labels;
    candiGraphData.data.datasets[0].data = data;

    //Party
    republicanVote = candiData.trump + candiData.mike + candiData.halley;
    democraticVote = candiData.harris + candiData.joe + candiData.obama;
    thirdVote = candiData.west + candiData.oliver + candiData.kennedy;
    remainVote = 20 - republicanVote - democraticVote - thirdVote;
    
    partyGraphData.data.labels = [
        'Republican Party',
        'Democratic Party',
        'Third Party',
        'Remain vote'
    ]
    
    partyGraphData.data.datasets[0].data = [
        republicanVote,
        democraticVote,
        thirdVote,
        remainVote
        // democraticVote,
        // thirdVote
    ];

    candiChart.update();
    partyChart.update();
}

