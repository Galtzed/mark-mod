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

export async function checkToken() : Promise<boolean>
    {
        return cookies().get("token")!=undefined;
    }

export async function sendAuth(token:string,APIendpoint:string): Promise<any> {
    await axios.post(`http://localhost:8000/${APIendpoint}/`,
    {
        Authorization: "Token "+token
    },{headers:{'Content-Type': 'application/json'}}).then((res)=>{
        
    })
}

export async function GetGroup(APIendpoint:string): Promise<string[]> {
    var data : any;
    await axios.get(`http://localhost:8000/${APIendpoint}/`,{headers:{'Content-Type': 'application/json',Authorization: "Token "+cookies().get("token")}})
    .then((res)=>{
        var arr : string[] = new Array()
        res.data.foreach((e:any)=>arr.push(e.group))
        data = arr;
    })
    .catch(e=>{})
    return data;

}