import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';
const myWork = [
    {
        'title':"Work Example 1",
        'href' : 'https://google.com',
        'desc': 'sdcscd',
        'image':{
            'desc':'example screenshot of project',
            'src':'images/example1.png',
            'comment':'',
        }
    },
    {
        'title':"Work Example 2",
        'href' : 'https://google.com',
        'desc': 'sdcscd',
        'image':{
            'desc':'example screenshot of project',
            'src':'images/example2.png',
            'comment':'',
        }
    },
    {
        'title':"Work Example 3",
        'href' : 'https://google.com',
        'desc': 'sdcscd',
        'image':{
            'desc':'example screenshot of project',
            'src':'images/example3.png',
            'comment':'',
        }
    }
]
ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'))