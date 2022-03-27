import React, {useState} from 'react'
import {Form, Button, Card} from 'react-bootstrap'

function Login() {
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')

    const handleSubmit = (e) => {
        console.log("WORKS!")
        console.log(email)
        console.log(password)
        e.preventDefault()
    }

  return (
<Card>
        <Card.Body>
            <h2 className = "text-center mb-4 "> Sign Up</h2>
            <Form>
                <Form.Group id = "email">
                    <Form.Label>Email</Form.Label>
                    <Form.Control 
                    type = "email" 
                    placeholder='Email' 
                    value = {email} 
                    name = "email"  r
                    onChange = {(e)=> {setEmail(e.target.value)}}
                    equired/>
                </Form.Group>

                <Form.Group id = "password">
                    <Form.Label>Password</Form.Label>
                    <Form.Control 
                    type = "password" 
                    placeholder='Password' 
                    value = {password} 
                    name = "password" 
                    onChange = {(e)=> {setPassword(e.target.value)}}
                    required/>
                </Form.Group>
                <br/>


                <Button onClick={handleSubmit} className = "w-100" type  = "submit">Login</Button>
            </Form>
        </Card.Body>
    </Card>
  )
}

export default Login