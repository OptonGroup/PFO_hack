import './App.scss';
import Database from './components/Database.js';
import NavBar from './components/NavBar.js';
import Stats from './components/Stats.js';

function App() {
	return (
		<div className='App w-100 h-100'>
			<NavBar/>
			<div className='menu'>
				<Stats/>
				<Database/>
			</div>
		</div>
	);
}

export default App;
