'use server'
import { cookies } from "next/headers"
import axios from "axios";

export async function setToken(Username : string, Password : string) : Promise<void> {
    var token : any ;
    await axios.post("http://localhost:8000/api-token-auth/",
    {
        username : Username,
        password : Password
    },{headers:{'Content-Type': 'application/json'}}).then((res)=>{
        token = res.data.token
    }).catch(
        err=>{}
    )
    cookies().set("token",token);
}

export async function checkToken() : Promise<boolean>{
    return cookies().get("token")!=undefined;
}

export async function GetGroup(): Promise<string[]> {
    var data : any;
    console.log(cookies().get("token"));
    await axios.get(`http://localhost:8000/GetGroup/`,{headers:{'Content-Type': 'application/json',Authorization: "Token "+cookies().get("token")?.value}})
    .then((res)=>{
        var arr : string[] = new Array()
        for(var index in res.data){
            console.log(res.data[index]);
            arr.push(res.data[index].name);
        }
        data = arr;
    })
    .catch(e=>{})
    return data;
}