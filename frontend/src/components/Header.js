import React, {useContext} from 'react';
import { Navbar, Nav, NavDropdown }from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChartBar } from '@fortawesome/free-solid-svg-icons';
import {Link} from 'react-router-dom';
import {AuthContext} from './AuthContext';

function Header() {
    const [state, setState] = useContext(AuthContext);

    const UserNameDropDown= (props) => {
        return (
            <NavDropdown alignRight title={props.username}  id="username-dropdown">
                 <NavDropdown.Item as={Link} to="/myteams">My Teams</NavDropdown.Item>
                 <NavDropdown.Item as={Link} to="/" onClick={() => setState({})}>Logout</NavDropdown.Item>
             </NavDropdown>
        );
    }

    let username;
    username = state.name ? <UserNameDropDown username={state.name}/> :  <Navbar.Text><Link to="/login">Login</Link></Navbar.Text>

    return (
        <Navbar collapseOnSelect expand="lg" sticky="top" bg="dark" variant="dark">
            <Navbar.Brand as={Link} to="/">
                Sport Stat Tracker {' '}
                <FontAwesomeIcon icon={faChartBar}/>
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="mr-auto">
                <Nav.Link as={Link} exact to="/teams">Teams</Nav.Link>
                <Nav.Link as={Link} to="/players">Players</Nav.Link>
            </Nav>
            <Nav>
                {username}
            </Nav>
            </Navbar.Collapse>
        </Navbar> 
    )
}

export default Header
