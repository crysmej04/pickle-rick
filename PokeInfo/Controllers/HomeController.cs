using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace pokeinfo.Controllers
{
    public class HomeController : Controller
    {
        // GET: /Home/
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }

        // GET: /pokemon/pokeid
        [HttpGet]
        [Route("pokemon/{pokeid}")]
        public IActionResult QueryPoke(int pokeid)
        {
            var CurrPokemon = new Pokemon();
            
            WebRequest.GetPokemonDataAsync(pokeid, ApiResponse =>
                {
                    CurrPokemon = ApiResponse;
                    Console.WriteLine("========================================================CurrPokemon: "+CurrPokemon);
                }
            ).Wait();
            Console.WriteLine("Waiting ====== Waiting =========== Waiting ========= Waiting ==========");
            ViewBag.Pokemon = CurrPokemon;
            return View("Index");
        }    
    }
}