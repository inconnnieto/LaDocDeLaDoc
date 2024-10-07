import liste from './liste.json' assert {type: 'json'}

function groupe(k){
    if(k < 1){throw new Error("nan")}
    let l = [...liste]
    l.sort((a, b) => Math.random() - 0.5)
    let result = []
    while(l.length > 0){
        result.push(l.splice(0,k))
    }
    return result
}
