import './Database.scss';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Database(){
    const [location, ChangeLocation] = useState('Республика Татарстан')
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:5000/data/${location}`);
                setData(response.data);
                console.log(response)
            } catch (err) {
                alert(`Error ${err}`);
            }
        };

        fetchData();
    }, [location]);

    return(
        <div className="Database">
            <div class="container">
<div class="row">
    <div class="col-lg-12 card-margin">
        <div class="card search-form">
            <div class="card-body p-0">
                <form id="search-form">
                    <div class="row">
                        <div class="col-12">
                            <div class="row no-gutters">
                                <div class="col-lg-3 col-md-3 col-sm-12 p-0">
                                    <select class="form-control" id="exampleFormControlSelect1" value={location} onChange={(e) => ChangeLocation(e.target.value)} >
                                        <option>Владимирская область</option>
                                        <option>Кировская область</option>
                                        <option>Нижегородская область</option>
                                        <option>Республика Марий Эл</option>
                                        <option>Республика Мордовия</option>
                                        <option>Республика Татарстан</option>
                                        <option>Республика Удмуртия</option>
                                        <option>Республика Чувашия</option>
                                    </select>
                                </div>
                                <div class="col-lg-8 col-md-6 col-sm-12 p-0">
                                    <input type="text" placeholder="Search..." class="form-control" id="search" name="search"/>
                                </div>
                                <div class="col-lg-1 col-md-3 col-sm-12 p-0">
                                    <button type="submit" class="btn btn-base">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-search"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
<div class="row">
        <div class="col-12">
            <div class="card card-margin">
                <div class="card-body">
                    <div class="row search-body">
                        <div class="col-lg-12">
                            <div class="search-result">
                                <div class="result-body">
                                    <div class="table-responsive">
                                        <table class="table widget-26">
                                        <thead>
                                            <tr class="text-gray-400">
                                                <th class="font-normal px-3 pt-0 pb-3 border-b border-gray-200 dark:border-gray-800">ID компании</th>
                                                <th class="font-normal px-3 pt-0 pb-3 border-b border-gray-200 dark:border-gray-800">Тип Бизнеса</th>
                                                <th class="font-normal px-3 pt-0 pb-3 border-b border-gray-200 dark:border-gray-800 hidden md:table-cell">Вероятность ухода</th>
                                                <th class="font-normal px-3 pt-0 pb-3 border-b border-gray-200 dark:border-gray-800">Уровень опасности</th>
                                            </tr>
                                        </thead>
                                            <tbody>                                              
                                                {data.map((item) => (
                                                    <tr>
                                                        <td>
                                                            <div class="widget-26-job-title">
                                                                <a href="#">{item['ID']}</a>
                                                            </div>
                                                        </td>
                                                        <td>
                                                            <div class="widget-26-job-info">
                                                                <p class="type m-0">{item['Company']}</p>
                                                            </div>
                                                        </td>
                                                        <td>
                                                            <div class="widget-26-job-salary">{item['Score']}%</div>
                                                        </td>
                                                        <td>
                                                            <div class={"widget-26-job-category indicator-wrap " + ((item['Score'] < 33) ? 'bg-soft-success' : ( (item['Score'] < 66) ? 'bg-soft-warning' : 'bg-soft-danger'))}>
                                                                <i class={"indicator " + ((item['Score'] < 33) ? 'bg-success' : ( (item['Score'] < 66) ? 'bg-warning' : 'bg-danger'))}></i>
                                                                <span>{
                                                                    (item['Score'] < 33) ? 'OK' : ( (item['Score'] < 66) ? 'Warning' : 'Danger')
                                                                }</span>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                ))}

                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
        </div>

        
    )
}

export default Database;