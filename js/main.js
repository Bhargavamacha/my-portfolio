import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';
const myWork = [
    {
        'title':"Work Example 1",
        'image':{
            'desc':'example screenshot of project',
            'src':'images/example1.png',
            'comment':'',
        }
    },
    {
        'title':"Work Example 2",
        'image':{
            'desc':'example screenshot of project',
            'src':'images/example2.png',
            'comment':'',
        }
    },
    {
        'title':"Work Example 3",
        'image':{
            'desc':'example screenshot of project',
            'src':'images/example3.png',
            'comment':'',
        }
    }
]
ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'))